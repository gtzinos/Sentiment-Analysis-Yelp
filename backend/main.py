from flask import Flask, jsonify
from flask_cors import CORS

from backend.dbQueries.restaurants import *
from backend.dbQueries.reviews import *
from backend.dbQueries.users import *
from backend.mlClassifiers.datasetController.mlDataframeCreator import *
from backend.mlClassifiers.mlModels.deepNeuralNetwork import DeepNeuralNetwork
from backend.mlClassifiers.mlModels.naiveBayes import NaiveBayes
from backend.mlClassifiers.mlModels.svm import SVM_clf

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
            #row[fieldName] = remove_punctuation(row[fieldName])
            row[fieldName] = replace_numbers(row[fieldName])
            row[fieldName] = remove_stopwords(row[fieldName])
            row[fieldName] = stem_en_words(row[fieldName])

    return dataList


def main():
    global db
    ''' SINCE I HAVE CREATED THEM, there is the csv file in resource, UNCOMMENT to run it from the start
        and delete the dataset.csv from resources to create it from the start.
        Loading reviews from mongodb, create dataset and save it.
        the first time we get the filtered reviews, the dataframe with the standard preprocess is created and
        saved to memory (resource/dataset.csv), if the file exist, it load it instead'''
    # db = openConnection(db_hostname, db_name, db_port)
    #
    # filteredReviews = ML_DatasetCreator(reviewTableName=db_reviews_table_name,
    #                                     userTableName=db_users_table_name,
    #                                     restaurantTableName=db_restaurants_table_name)
    #
    # mlDataframeCreator = ML_DataframeCreator(filtered_reviews=filteredReviews
    #                                          .get_filtered_ml_reviews(db, typeOfRestaurant="Japanese"),
    #                                          features_to_keep=['text', 'stars'])
    #
    # dataframe = mlDataframeCreator.get_columns_of_interesting()
    # mlDataframeCreator.preprocess(dataframe=dataframe)
    ''' creation of dataset finished '''

    samplePositiveReview = "The crust is different. I don't care what anyone says," \
                           " the crust is thicker than the crust at their Rancho location." \
                           " I've been eating regularly at the Rancho location since they opened in 1996." \
                           " And when I say regularly, I mean weekly. I'm sure I've ordered several hundred pies from this place," \
                           " so I know what I'm talking about. The crust at the Sahara location is definitely a little thicker. " \
                           "But even if that is indeed the case, it's still the wonderful greasy New York pizza that I've come to" \
                           " love and crave. I highly recommend the cheese pizza. I am not  normally a cheese only kind of gal," \
                           " but there's something special about their cheese blend - it's just so sweet and luscious. And their buttery" \
                           " warm garlic knots...mmmmmmmm! Chicken fingers and wings are available in plain, mild," \
                           " medium or hot and their french fries are big and thick, no shoestring fries here. Tableside service " \
                           "and quick and friendly."
    sampleNegativeReview = "I don't recommend. I like the store but the food part 'taqueria' is always dirty." \
                           " The meat has a taste like it's been sitting out for a while. I won't try this place again."

    sampleNegativeReview3 = "That wasnt good place to eat, terrible food and general bad environment." \
                            " The meat has a taste like it's been sitting out for a while. I won't try this place again."

    sampleNegativeReview4 = "Still quite poor both in service and food. maybe I made a mistake and ordered Sichuan Gong Bao ji ding for what seemed like people from canton district. Unfortunately to get the good service U have to speak Mandarin/Cantonese. I do speak a smattering but try not to use it as I never feel confident about the intonation. \n\nThe dish came out with zichini and bell peppers (what!??)  Where is the peanuts the dried fried red peppers and the large pieces of scallion. On pointing this out all I got was ' Oh you like peanuts.. ok I will put some on' and she then proceeded to get some peanuts and sprinkle it on the chicken.\n\nWell at that point I was happy that atleast the chicken pieces were present else she would probably end up sprinkling raw chicken pieces on it like the raw peanuts she dumped on top of the food. \n\nWell then  I spoke a few chinese words and the scowl turned into a smile and she then became a bit more friendlier. \n\nUnfortunately I do not condone this type of behavior. It is all in poor taste..."

    sampleNegativeReview5 = "Other than the really great happy hour prices, its hit or miss with this place.Not good food and i despice the people there. More often a miss. :(\n\nThe food is less than average, the drinks NOT strong ( at least they are inexpensive) , but the service is truly hit or miss.\n\nI'll pass."

    ''''DNN'''
    dnnModel = DeepNeuralNetwork("dataset.csv")
    dnnModel.trainModel()
    dnnModel.predict(samplePositiveReview)
    dnnModel.predict(sampleNegativeReview)
    dnnModel.predict(sampleNegativeReview3)
    dnnModel.predict(sampleNegativeReview4)
    dnnModel.predict(sampleNegativeReview5)
    ''''DNN'''

    ''''NaiveBayes'''
    nbModel = NaiveBayes("dataset.csv")
    nbModel.trainModel()
    nbModel.predict(samplePositiveReview)
    nbModel.predict(sampleNegativeReview)
    nbModel.predict(sampleNegativeReview3)
    nbModel.predict(sampleNegativeReview4)
    nbModel.predict(sampleNegativeReview5)
    ''''NaiveBayes'''

    ''' SVM '''
    svmModel = SVM_clf("dataset.csv")
    svmModel.trainModel()
    svmModel.predict(samplePositiveReview)
    svmModel.predict(sampleNegativeReview)
    svmModel.predict(sampleNegativeReview3)
    svmModel.predict(sampleNegativeReview4)
    svmModel.predict(sampleNegativeReview5)
    ''' SVM '''

    reviews = Reviews(name=db_reviews_table_name)

    data = reviews.get_filtered_reviews(db, 1, 10)

    print(data)

    data = preprocessing(data, ["text"])

    print(data)


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

    reviews = Restaurants(name=db_restaurants_table_name).get_restaurants_by_wifi(db)

    return jsonify(reviews)

@app.route("/users-per-year")
def getUsersPerYear():
    db = openConnection(db_hostname, db_name, db_port)

    users = Users(name=db_users_table_name).get_users_per_year(db,15)

    return jsonify(users)
# print(top)
# if __name__ == "__main__":
    # main()
