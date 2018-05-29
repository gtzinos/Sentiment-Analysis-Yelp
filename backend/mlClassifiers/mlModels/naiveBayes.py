from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

import dataAnalysis.filterData as preprocess
from mlClassifiers.dao.mlReadWriteCSV import checkFileExistance, loadDataframeFromMemory
from mlClassifiers.datasetController.mlDataframeCreator import createDataframeFromScrach, preprocessReview, \
  listOfStringToString


class NaiveBayes:
  def __init__(self, dataframeName=None):
    self.vect = CountVectorizer()
    # self.tfidf_transformer = TfidfTransformer()
    self.initDataframe(dataframeName)

  def initDataframe(self, fileName):
    fileExistance = checkFileExistance(fileName)
    self.prepareDatasetForNB(fileExistance, fileName)

  def trainModel(self):
    self.splitDataset()
    self.model = MultinomialNB()
    self.model.fit(self.X_train_dtm, self.trainY)
    self.y_pred_class = self.model.predict(self.X_test_dtm)
    from sklearn import metrics
    print("ACCURACY NB :"+str(metrics.accuracy_score(self.testY, self.y_pred_class)))
    print("PRECISION NB :" + str(metrics.precision_score(self.testY, self.y_pred_class)))
    print("RECALL NB :" + str(metrics.recall_score(self.testY, self.y_pred_class)))
    print("F1 NB :" + str(metrics.f1_score(self.testY, self.y_pred_class)))

  ''' method that gets a review, tranform it to a vector and predicts its output '''
  def predict(self, review):
    processedReview = preprocessReview(review, "nb", vectorizer=self.vect, tf_idf=None, isSingle=True)
    prediction = self.model.predict(processedReview)
    print("Prediction from NB: %s" % str(prediction[0]))
    return prediction

  def prepareDatasetForNB(self, fileExistance, fileName):
    if fileExistance is True:
      self.dataframe = loadDataframeFromMemory(fileName)
    else:
      self.dataframe = createDataframeFromScrach()

    self.dataframe['stars'] = self.dataframe.apply(lambda row: preprocess.label_to_binary(row["stars"]), axis=1)
    self.dataframe['text'] = self.dataframe['text'].apply(lambda row: listOfStringToString(row))



  '''Extra preprocess that our data needs, '''

  def splitDataset(self):
    self.train, self.test = train_test_split(self.dataframe, test_size=0.3)
    self.trainX, self.trainY = self.train.iloc[:, 0], self.train.iloc[:, 1]
    self.testX, self.testY = self.test.iloc[:, 0], self.test.iloc[:, 1]

    self.extraPreprocessForNB()

  def extraPreprocessForNB(self):
    self.X_train_dtm = self.vect.fit_transform(self.trainX)
    self.X_test_dtm = self.vect.transform(self.testX)

    # self.X_train_tfidf = self.tfidf_transformer.fit_transform(self.X_train_dtm)
    # self.X_test_tfidf = self.tfidf_transformer.fit_transform(self.X_test_dtm)

    # print(self.X_train_dtm)
