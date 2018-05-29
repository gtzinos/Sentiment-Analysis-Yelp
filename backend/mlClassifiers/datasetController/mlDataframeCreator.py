import pandas as pd
import dataAnalysis.filterData as preprocess
from tflearn.data_utils import pad_sequences
from config.database import db_hostname, db_name, db_port, db_reviews_table_name, db_users_table_name, \
  db_restaurants_table_name
from dbQueries.connect import openConnection
from mlClassifiers.dao.mlReadWriteCSV import *
from mlClassifiers.datasetController.mlDbQueriesController import ML_DatasetCreator


class ML_DataframeCreator:

  ''' init of ML_DataframeCreator : give filteredReviews, and features that we are interested in this dataframe (text,stars)'''
  def __init__(self, filtered_reviews, features_to_keep=None):

    if features_to_keep is None:
      features_to_keep = []

    self.features_to_keep = features_to_keep
    self.filtered_reviews = filtered_reviews
    self.cstExistence = checkFileExistance("dataset.csv")

  ''' keep the columns we need for machine learning algorithms, ie "text" and "stars" '''
  def get_columns_of_interesting(self):

    reviewsAndLabelDf = pd.DataFrame(list(self.filtered_reviews))

    new_data = reviewsAndLabelDf[self.features_to_keep]

    return new_data

  ''' Preprocess the dataframe, and if it doesnt exist in resources save it.
      otherwise load it from resources and skip preprocess step '''
  def preprocess(self, dataframe):
    if self.cstExistence is False:
      dataframe['text'] = dataframe.apply(lambda row: preprocess.tokenization(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.replace_emoticons(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.replace_slang_internet_words(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.replace_negation_words(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.remove_punctuation_preprocess(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.remove_empty_words(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.replace_laughs(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.replace_emphasis_on_words(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.replace_laugh_sequences(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.to_lowercase(row["text"]), axis=1)
      # dataframe['text'] = dataframe.apply(lambda row: preprocess.snowball_stemmer(row["text"]), axis=1)
      dataframe['text'] = dataframe.apply(lambda row: preprocess.remove_stopwords_with_custom_list(row["text"]), axis=1)
      dataframe['stars'] = dataframe.apply(lambda row: preprocess.stars_to_label(row["stars"]), axis=1)
      dataframe.to_csv("../resources/dataset.csv", encoding='utf-8')
    else:
      dataframe = loadDataframeFromMemory("dataset.csv")

    return dataframe

''' loading reviews from mongodb, create dataset and save it to memory, will run once '''
def createDataframeFromScrach():

  db = openConnection(db_hostname, db_name, db_port)

  filteredReviews = ML_DatasetCreator(reviewTableName=db_reviews_table_name,
                                      userTableName=db_users_table_name,
                                      restaurantTableName=db_restaurants_table_name)

  mlDataframeCreator = ML_DataframeCreator(filtered_reviews=filteredReviews
                                           .get_filtered_ml_reviews(db, typeOfRestaurant="Japanese"),
                                           features_to_keep=['text', 'stars'])

  dataframe = mlDataframeCreator.get_columns_of_interesting()
  preprocessedDF = mlDataframeCreator.preprocess(dataframe=dataframe)

  return preprocessedDF

''' Preprocess of a single review, used from the prediction methods of our algorithms '''
def preprocessReview(review,model=None,tokenizer=None,isSingle=None,vectorizer=None,tf_idf=None):
  if model=="dnn":
    review = preprocess.tokenization(review)
    review = preprocess.replace_emoticons(review)
    review = preprocess.replace_slang_internet_words(review)
    review = preprocess.replace_negation_words(review)
    review = preprocess.remove_punctuation_preprocess(review)
    review = preprocess.remove_empty_words(review)
    review = preprocess.replace_laughs(review)
    review = preprocess.replace_emphasis_on_words(review)
    review = preprocess.replace_laugh_sequences(review)
    review = preprocess.to_lowercase(review)
    # review = preprocess.snowball_stemmer(review)
    review = preprocess.remove_stopwords_with_custom_list(review)
    review = tokenizer.texts_to_sequences(review)
    review = getSingleList(review)
    if isSingle:
      if len(review)>130:
        review = review[:-(len(review)-130)]
      else:
        review = pad(review, 0, 130)
    else:
      review = pad_sequences(review, maxlen=130, value=0.)
    # print(np.shape(review))
    # review = toListOfLists(review)
  elif model=="nb" or model=="svm":
    review = preprocess.tokenization(review)
    review = preprocess.replace_emoticons(review)
    review = preprocess.replace_slang_internet_words(review)
    review = preprocess.replace_negation_words(review)
    review = preprocess.remove_punctuation_preprocess(review)
    review = preprocess.remove_empty_words(review)
    review = preprocess.replace_laughs(review)
    review = preprocess.replace_emphasis_on_words(review)
    review = preprocess.replace_laugh_sequences(review)
    review = preprocess.to_lowercase(review)
    # review = preprocess.snowball_stemmer(review)
    review = preprocess.remove_stopwords_with_custom_list(review)
    review = listOfStringToString(review)
    review = vectorizer.transform([review])
  else:
    review = preprocess.tokenization(review)
    review = preprocess.replace_emoticons(review)
    review = preprocess.replace_slang_internet_words(review)
    review = preprocess.replace_negation_words(review)
    review = preprocess.remove_punctuation_preprocess(review)
    review = preprocess.remove_empty_words(review)
    review = preprocess.replace_laughs(review)
    review = preprocess.replace_emphasis_on_words(review)
    review = preprocess.replace_laugh_sequences(review)
    review = preprocess.to_lowercase(review)
    # review = preprocess.snowball_stemmer(review)
    review = preprocess.remove_stopwords_with_custom_list(review)

  return review

def pad(list, content, width):
    list.extend([content] * (width - len(list)))
    return list

def changeOrderOfList(list):
  resultList=[]
  for x in list:
    resultList.append(x)
  return resultList

''' we need to tranform our review vector from a list of ints to a list of list ints, (300,)=>(300,1) '''
def toListOfLists(list):
  flat_list = []
  for item in list:
      flat_list.append([item])
  return flat_list

def getSingleList(listOfSublists):
  flat_list = [item for sublist in listOfSublists for item in sublist]

  return flat_list

def listOfStringToString(row):

  stringResult = ','.join(row)

  return stringResult
