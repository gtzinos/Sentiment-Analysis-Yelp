from flask import Flask, json, Response, jsonify, request
from flask_cors import CORS
from config.http_codes import HttpCodes
from dbQueries.maps import *
from bson.json_util import dumps

from dbQueries.restaurants import *
from dbQueries.reviews import *
from dbQueries.users import *
from mlClassifiers.datasetController.mlDataframeCreator import *
from mlClassifiers.mlModels.deepNeuralNetwork import DeepNeuralNetwork
from mlClassifiers.mlModels.naiveBayes import NaiveBayes
from mlClassifiers.mlModels.svm import SVM_clf
from config.database import *
from dbQueries.connect import *
from dbQueries.restaurants import *
from dbQueries.reviews import *
from dbQueries.restaurants2 import *
from dbQueries.users import *
from dataAnalysis.filterData import *
from dataAnalysis.plots import *
from dataAnalysis.training import *

app = Flask(__name__)

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

@app.route("/group-users-by", methods=['POST'])
def getGroupedUsersBy():
    fieldName = request.get_json().get('fieldName')

    db = openConnection(db_hostname, db_name, db_port)

    users = Users(name=db_users_table_name).get_users_grouped_by(db, fieldName)

    return jsonify(users)

@app.route("/top-words")
def getTopWords():
    db = openConnection(db_hostname, db_name, db_port)

    reviews = Reviews(name=db_reviews_table_name).get_top_words(db, 10)

    allReviewsTexts = ""

    frequency = {}

    for review in reviews:
        review['text'] = tokenization(review['text'])
        review['text'] = remove_non_words(review['text'])
        review['text'] = remove_stopwords(review['text'])

        for word in review['text']:
            if word not in frequency:
                frequency[word] = 0

            frequency[word] += 1

    sortedArray = []

    for key in frequency:
        sortedArray.append({"id": key, "frequency": frequency[key]})

    sortedArray = sorted(
        sortedArray, key=lambda k: k['frequency'])
    sortedLength = len(sortedArray)

    return Response(json.dumps({"message": sortedArray[sortedLength - 21: sortedLength]}),
                    status=HttpCodes.HTTP_OK_BASIC,
                    mimetype='application/json')


@app.route("/maps")
def getAllRestaurans():
    limit = int(request.args.get('limit'))

    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Maps(name=db_restaurants_table_name).find_restaurants(db, limit)

    output = []
    for rest in restaurants:
        output.append(rest)

    return jsonify(output)


@app.route("/maps/5stars")
def getFiveStarRestaurans():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Maps(
        name=db_restaurants_table_name).find_5star_restaurants(db,200)

    output = []
    for rest in restaurants:
        output.append(rest)

    return jsonify(output)

@app.route("/maps/wifi")
def getWifiRestaurants():
    stars = int(request.args.get('stars'))
    limit = int(request.args.get('limit'))

    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Maps(
        name=db_restaurants_table_name).find_wifi_restaurants(db, stars, limit)

    output = []
    for rest in restaurants:
        output.append(rest)

    return jsonify(output)

@app.route("/maps/wifi_tv")
def getWifiTvRestaurants():
    stars = int(request.args.get('stars'))
    limit = int(request.args.get('limit'))

    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Maps(
        name=db_restaurants_table_name).find_wifi_tv_restaurants(db, stars, limit)

    output = []
    for rest in restaurants:
        output.append(rest)

    return jsonify(output)


@app.route("/maps/gfk_hh_os")
def get_gfk_hh_os_rest():
    stars = int(request.args.get('stars'))
    limit = int(request.args.get('limit'))

    db = openConnection(db_hostname, db_name, db_port)

    if(limit == 0):
        restaurants = Maps(name=db_restaurants_table_name).find_gfk_hh_os_rest_no_limit(db,stars)
    else:
        restaurants = Maps(name=db_restaurants_table_name).find_gfk_hh_os_rest(db,stars, limit)

    output = []
    for rest in restaurants:
        output.append(rest)

    return jsonify(output)

@app.route("/restaurants-by-groups")
def getRestaurantsByGroup():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_restaurants_by_neighborhood(db)

    return jsonify(restaurants)

@app.route("/restaurants-by-meals")
def getRestaurantsByMeals():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_restaurants_by_meals(db)

    return jsonify(restaurants)

@app.route("/restaurants-by-ambience")
def getRestaurantsByAbmience():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_restaurants_by_ambience(db)

    return jsonify(restaurants)

@app.route("/restaurants-by-music")
def getRestaurantsByMusic():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_restaurants_by_music(db)

    return jsonify(restaurants)

@app.route("/restaurants-by-day")
def getRestaurantsByDay():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_restaurants_by_day(db)

    return jsonify(restaurants)

@app.route("/best-restaurant-by-neighborhood")
def getBestRestaurant():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_best_restaurants_by_neighborhood(db)

    return jsonify(restaurants)

@app.route("/top10-quiet-restaurants")
def getTop10Quiet():
    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_top10_quiet_restaurants_by_neighborhood(db)

    return jsonify(restaurants)

@app.route("/smoking-by-neighborhood")
def getSmokingNeighborhood():
    neighborhood = request.args.get('neighborhood')

    db = openConnection(db_hostname, db_name, db_port)

    restaurants = Restaurants2(name=db_restaurants_table_name).get_smoking_neighborhood(db,neighborhood)

    return jsonify(restaurants)

app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
