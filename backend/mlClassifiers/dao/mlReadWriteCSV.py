import csv

from pandas import DataFrame
from pathlib import Path
from dataAnalysis.filterData import *

def readCsvFile(dataset):

  with open(dataset, encoding="utf8") as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')

    text = []
    stars = []

    for row in readCSV:
      filteredReviewList = remove_punctuation_preprocess(str(row[1]).split("'"))
      filteredReviewList = remove_strip_words(filteredReviewList)
      text.append(filteredReviewList)
      stars.append(row[2])

    dataframe = DataFrame({'stars': stars, 'text': text})
    cols = ['text', 'stars']
    dataframe = dataframe[cols]
    dataframe.drop(dataframe.index[:1], inplace=True)

    return dataframe

# def concatenateAllWordsFromColumn(dataframe):
#   lists = ""
#
#   for index, row in dataframe.iterrows():
#     lists += ','.join(map(str, row['text']))
#
#   return lists

# def listOfStringToString(row):
#
#   stringResult = ','.join(row)
#
#   return stringResult

# def createListOfWords(concatenatedWords):
#   concatenatedWords = concatenatedWords.split(',')
#
#   return concatenatedWords

# def getDictionarySize(dataframe):
#   concatenatedWords = concatenateAllWordsFromColumn(dataframe)
#   listOfWords = createListOfWords(concatenatedWords)
#
#   count = len(set(listOfWords))
#
#   return count

# def getTrainedTokenizedDictionary(dataframe, lengthOfDictionary):
#   tokenizer = Tokenizer(num_words=lengthOfDictionary)
#   texts = concatenateAllWordsFromColumn(dataframe)
#   listOfWords = createListOfWords(texts)
#
#   tokenizer.fit_on_texts(listOfWords)
#   return tokenizer

''' loading preprocessed dataframe from memory resources, still will need '''
def loadDataframeFromMemory(fileName):
  filePath = "../resources/"+fileName
  dataframe = readCsvFile(filePath)

  return dataframe

''' checking file existance in resources '''

def checkFileExistance(fileName):
  filePath = "../resources/" + fileName
  my_file = Path(filePath)
  if my_file.is_file():
    return True
  else:
    return False

def dnnModelExist(filePath):
  my_file = Path(filePath)
  if my_file.is_file():
    return True
  else:
    return False
