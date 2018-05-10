from flask import Flask, render_template
from config import *
from db_queries import *
from data_analysis import *

db = openConnection(db_hostname, db_name, db_port)

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


#top = find_count(db, "reviews")

#print(top)
if __name__ == "__main__":
    main()
