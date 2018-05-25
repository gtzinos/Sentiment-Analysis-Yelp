from flask import Flask, jsonify, request
from backend.config.database import *
from backend.dbQueries.connect import *
from backend.dbQueries.restaurants import *
from backend.dbQueries.reviews import *
from backend.dbQueries.users import *
from backend.dataAnalysis.filterData import *
from backend.dataAnalysis.plots import *
from backend.dataAnalysis.training import *
from bson.json_util import dumps
from flask_cors import CORS


import pip
print(pip.__version__)

db = openConnection(db_hostname, db_name, db_port)

app = Flask(__name__)
app.Debug = True

CORS(app)


def preprocessing(dataList, fieldNames):
    for fieldName in fieldNames:
        print(fieldName)
        for row in dataList:
            print(row)

            row[fieldName] = tokenization(row[fieldName])
            row[fieldName] = remove_non_ascii(row[fieldName])
            row[fieldName] = to_lowercase(row[fieldName])
            # row[fieldName] = remove_punctuation(row[fieldName])
            row[fieldName] = replace_numbers(row[fieldName])
            row[fieldName] = remove_stopwords(row[fieldName])
            row[fieldName] = stem_en_words(row[fieldName])

    return dataList


def main():
    global db

    reviews = Reviews(name=db_reviews_table_name)

    data = reviews.get_filtered_reviews(db, 1, 10)

    print(data)

    data = preprocessing(data, ["text"])

    print(data)
    # seaborn(data)


@app.route("/restaurants")
def restaurants():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants(
        name=db_restaurants_table_name).find_top_restaurants(db, 10)

    output = []
    for rest in restaurants:
        output.append(rest)

    return jsonify(output)


@app.route("/reviews")
def reviews():
    db = openConnection(db_hostname, db_name, db_port)

    reviews = Reviews(name=db_reviews_table_name).find_top_reviews(db, 10)

    output = []
    for review in reviews:
        output.append(
            {"text": str(review['text']), "totalUseful": review['totalUseful']})

    return jsonify(output)


@app.route("/users")
def users():
    db = openConnection(db_hostname, db_name, db_port)

    users = Users(name=db_users_table_name).find_top_users(db, 10)

    output = []
    for user in users:
        output.append({"name": str(
            user['name']), "totalUseful": user['totalUseful'], "fans": user['fans']})

    return jsonify(output)


@app.route("/reviews-per-year")
def getReviewsNumberByYear():
    db = openConnection(db_hostname, db_name, db_port)

    reviews = Reviews(name=db_reviews_table_name).get_reviews_per_year(db, 13)

    return jsonify(reviews)


@app.route("/restaurants-by-wifi")
def getRestaurantsByWifi():
    db = openConnection(db_hostname, db_name, db_port)

    reviews = Restaurants(
        name=db_restaurants_table_name).get_restaurants_by_wifi(db)

    return jsonify(reviews)


@app.route("/users-per-year")
def getUsersPerYear():
    db = openConnection(db_hostname, db_name, db_port)

    users = Users(name=db_users_table_name).get_users_per_year(db, 15)

    return jsonify(users)

@app.route("/top-words")
def getTopWords():
    db = openConnection(db_hostname, db_name, db_port)

    reviews = Reviews(name=db_reviews_table_name).get_top_words(db, 10)

    allReviewsTexts = ""

    for review in reviews:
        review['text'] = remove_non_words(review['text'])
        review['text'] = tokenization(review['text'])
        review['text'] = remove_non_ascii(review['text'])
        review['text'] = replace_numbers(review['text'])
        review['text'] = remove_stopwords(review['text'])

        review['text'] = ' '.join([" " + str(text) for text in review['text']])

    return jsonify(reviews)

@app.route("/cnn", methods=['POST'])
def getCNNPrediction():
    termToClassify = request.get_json().get('term')

    prediction = 1 #TODO ADD CNN Function

    return jsonify({"algorithm": "cnn", "prediction": prediction})
# print(top)
# if __name__ == "__main__":
    # main()
