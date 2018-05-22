from flask import Flask, jsonify, request
from config.database import *
from dbQueries.connect import *
from dbQueries.restaurants import *
from dbQueries.reviews import *
from dbQueries.users import *
from dataAnalysis.filterData import *
from dataAnalysis.plots import *
from dataAnalysis.training import *
from bson.json_util import dumps

db = openConnection(db_hostname, db_name, db_port)

app = Flask(__name__)
app.Debug = True


def preprocessing(dataList, fieldNames):
    for fieldName in fieldNames:
        print(fieldName)
        for row in dataList:
            print(row)

            row[fieldName] = tokenization(row[fieldName])
            row[fieldName] = remove_non_ascii(row[fieldName])
            row[fieldName] = to_lowercase(row[fieldName])
            #row[fieldName] = remove_punctuation(row[fieldName])
            row[fieldName] = replace_numbers(row[fieldName])
            row[fieldName] = remove_stopwords(row[fieldName])
            row[fieldName] = stem_en_words(row[fieldName])

    return dataList

def main():
    global db

    reviews = Reviews(name = db_reviews_table_name)

    data = reviews.get_filtered_reviews(db,1, 10)

    print(data)

    data = preprocessing(data, ["text"])

    print(data)
    #seaborn(data)


@app.route("/restaurants")
def restaurants():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants(name = db_restaurants_table_name).find_top_restaurants(db, 10)

    output = []
    for rest in restaurants:
        output.append(rest)

    return jsonify(output)

@app.route("/reviews")
def reviews():
    db = openConnection(db_hostname, db_name, db_port)

    reviews = Reviews(name = db_reviews_table_name).find_top_reviews(db, 10)

    output = []
    for review in reviews:
        output.append({"text": str(review['text']), "totalUseful": review['totalUseful']})

    return jsonify(output)

@app.route("/users")
def users():
    db = openConnection(db_hostname, db_name, db_port)

    users = Users(name = db_users_table_name).find_top_users(db, 10)

    output = []
    for user in users:
        output.append({"name": str(user['name']), "totalUseful": user['totalUseful'], "fans": user['fans']})

    return jsonify(output)


#print(top)
#if __name__ == "__main__":
    #main()
