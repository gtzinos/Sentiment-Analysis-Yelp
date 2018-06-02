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
from flask import Flask, json, Response, jsonify, request
from flask_cors import CORS

''' SINCE I HAVE CREATED THEM, there is the csv file in resource, UNCOMMENT to run it from the start
    and delete the dataset.csv from resources to create it from the start.
    Loading reviews from mongodb, create dataset and save it.
    the first time we get the filtered reviews, the dataframe with the standard preprocess is created and
    saved to memory (resource/dataset.csv), if the file exist, it load it instead'''
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

app = Flask(__name__)

CORS(app)

@app.route("/dnn", methods=['POST'])
def getCNNPrediction():
    global dnnModel
    termToClassify = request.get_json().get('term')

    prediction = dnnModel.predict(termToClassify)

    return jsonify({"algorithm": "dnn", "prediction": str(prediction)})

@app.route("/svm", methods=['POST'])
def getSVMPrediction():
    global svmModel
    termToClassify = request.get_json().get('term')

    prediction = svmModel.predict(termToClassify)[0]

    return jsonify({"algorithm": "svm", "prediction": str(prediction)})

@app.route("/nb", methods=['POST'])
def getNBPrediction():
    global nbModel
    termToClassify = request.get_json().get('term')

    prediction = nbModel.predict(termToClassify)[0]

    return jsonify({"algorithm": "nb", "prediction": str(prediction)})

@app.route("/metrics", methods=['POST'])
def getMetrics():
    global nbModel

    nbMetrics = nbModel.getMetrics()
    svmMetrics = svmModel.getMetrics()
    dnnMetrics = dnnModel.getAccuracy()


    return jsonify({"id": "NB", "Accuracy": nbMetrics["Accuracy"],"Precision": nbMetrics["Precision"],"Recall": nbMetrics["Recall"],"F1": nbMetrics["F1"]},
                   {"id": "SVM", "Accuracy": svmMetrics["Accuracy"], "Precision": svmMetrics["Precision"],"Recall": svmMetrics["Recall"], "F1": svmMetrics["F1"]},
                   {"id": "DNN", "Accuracy": dnnMetrics["Accuracy"]})

app.run(host='0.0.0.0', port=5001, debug=False, use_reloader=False)
