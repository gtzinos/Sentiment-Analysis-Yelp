import tensorflow as tf
import tflearn
import dataAnalysis.filterData as preprocess
from sklearn.model_selection import train_test_split
from tflearn.data_utils import to_categorical
from mlClassifiers.datasetController.mlDataframeCreator import *
from keras.preprocessing.text import Tokenizer

''' To create and call DNN, simple call the following methods in sequence :
    1) init object
    2) train 
    3) for prediction simple call predict method sending the review in its text unprocessed form'''

class DeepNeuralNetwork:
  def __init__(self, dataframeName=None):
    self.initDataframe(dataframeName)

  def initDataframe(self, fileName):
    fileExistance = checkFileExistance(fileName)
    self.prepareDatasetForDNN(fileExistance, fileName)

  ''' Initialize our dataset, if the standard preprocessed version exists in memory load it,
      otherwise create it from scratch.
      Also we initialize the tokenizer'''

  def prepareDatasetForDNN(self, fileExistance, fileName):
    if fileExistance is True:
      self.dataframe = loadDataframeFromMemory(fileName)
    else:
      self.dataframe = createDataframeFromScrach()

    self.dataframe['stars'] = self.dataframe.apply(lambda row: preprocess.label_to_binary(row["stars"]), axis=1)
    self.distinctWordCount = getDictionarySize(self.dataframe)
    self.tokenizer = getTrainedTokenizedDictionary(self.dataframe, self.distinctWordCount)

  def initNetwork(self):
    # network building
    # first layer, input layer
    net = tflearn.input_data([None, 130])
    # second layer, embedding layer
    net = tflearn.embedding(net, input_dim=self.distinctWordCount, output_dim=128)
    # lstm layer, allows our network to remember data from the beginning of the sequence
    net = tflearn.lstm(net, 128, dropout=0.5)
    # fully connected layer
    net = tflearn.fully_connected(net, 2, activation='softmax')
    net = tflearn.regression(net, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy')
    return net

  ''' training of DNN '''

  def trainModel(self):
    self.splitDataset()

    tflearn.init_graph(num_cores=6, gpu_memory_fraction=0.2)
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True

    self.network = self.initNetwork()
    '''Checks if the model exists, if it is don't create it from the start '''
    if dnnModelExist("../resources/dnnModel.index") is True:
      self.model = tflearn.DNN(self.network, tensorboard_verbose=0)
      self.model.load('../resources/dnnModel', weights_only=True)
      self.totalAccuracy()
    else:
      self.model = tflearn.DNN(self.network, tensorboard_verbose=0)
      # training
      self.model.fit(self.trainX, self.trainY, n_epoch=10, validation_set=(self.testX, self.testY),
                     batch_size=None, snapshot_step=100, snapshot_epoch=False, show_metric=True, run_id="dense_model")
      self.model.save("../resources/dnnModel")

  ''' method that gets a review, tranform it to a vector and predicts its output '''
  def predict(self, review):
    processedReview = preprocessReview(review, "dnn", self.tokenizer, isSingle=True)
    prediction = self.model.predict([processedReview])
    prediction = self.getPrediction(prediction)
    print("Prediction from DNN: %s" % str(prediction))
    return prediction

  def getPrediction(self,a):
    x = np.round(a[0][0])
    y = np.round(a[0][1])

    if x == 0 and y == 1:
      return 1
    else:
      return 0

  def totalAccuracy(self):
    score = self.model.evaluate(self.testX, self.testY)
    accuracy = [("Accuracy",str(score[0] * 100))]
    return dict(accuracy)

  def getAccuracy(self):
    score = self.model.evaluate(self.testX, self.testY)
    accuracy = [("Accuracy", str(score[0] * 100))]
    return dict(accuracy)


  ''' Here we split the dataset into training and test sets, 0.1 % for test, '''

  def splitDataset(self):
    self.train, self.test = train_test_split(self.dataframe, test_size=0.1)
    self.trainX, self.trainY = self.train.iloc[:, 0], self.train.iloc[:, 1]
    self.testX, self.testY = self.test.iloc[:, 0], self.test.iloc[:, 1]

    self.extraPreprocessForNN()

  '''Extra preprocess that our data needs, '''

  def extraPreprocessForNN(self):
    self.trainX = self.trainX.apply(lambda row: self.tokenizer.texts_to_sequences(row))
    self.trainX = self.trainX.apply(lambda row: getSingleList(row))

    self.testX = self.testX.apply(lambda row: self.tokenizer.texts_to_sequences(row))
    self.testX = self.testX.apply(lambda row: getSingleList(row))

    self.trainX = pad_sequences(self.trainX, maxlen=130, value=0.)
    self.testX = pad_sequences(self.testX, maxlen=130, value=0.)

    self.trainY = to_categorical(self.trainY, nb_classes=2)
    self.testY = to_categorical(self.testY, nb_classes=2)

'''Create dictionary'''
def getTrainedTokenizedDictionary(dataframe, lengthOfDictionary):
  tokenizer = Tokenizer(num_words=lengthOfDictionary)
  texts = concatenateAllWordsFromColumn(dataframe)
  listOfWords = createListOfWords(texts)

  tokenizer.fit_on_texts(listOfWords)
  return tokenizer

'''Get dictionary distinct word count (size)'''
def getDictionarySize(dataframe):
  concatenatedWords = concatenateAllWordsFromColumn(dataframe)
  listOfWords = createListOfWords(concatenatedWords)

  count = len(set(listOfWords))

  return count

'''Concatenate all rows from a column of our dataframe into a single row'''
def concatenateAllWordsFromColumn(dataframe):
  lists = ""

  for index, row in dataframe.iterrows():
    lists += ','.join(map(str, row['text']))

  return lists

'''Create a list of words out of a single string with words seperated by "," '''
def createListOfWords(concatenatedWords):
  concatenatedWords = concatenatedWords.split(',')

  return concatenatedWords
