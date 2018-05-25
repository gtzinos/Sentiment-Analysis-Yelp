import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
import string
from nltk.stem.snowball import EnglishStemmer
import unicodedata
from nltk.tokenize import TweetTokenizer
import inflect
import re
from nltk.stem.lancaster import LancasterStemmer

nltk.download('stopwords')


def oneHotEncoding(data, indexes):
    for index in indexes:
        # Encode string to number (For field name area)
        toEncode = data[:, index]
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(np.array(toEncode))

        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

        # data = np.delete(data, index, 1)
        data = np.append(data, onehot_encoded, 1)

    # ***Delete old features***
    data = np.delete(data, indexes, 1)
    # Parse data to float
    data = data.astype(np.float32)

    return data


def normalize_array(array, indexes):
    for index in indexes:
        scaler = MinMaxScaler()
        data = array[:, index].reshape(-1, 1)
        scaler.fit(data)
        array[:, index] = np.array(scaler.transform(data).reshape(1, -1))

    return array

def remove_non_words(words):
    new_words = []
    for word in words:
        word = word.lower()
        filtered = re.sub(r'(?:https?|ftp|http):\/\/[\n\S]+', '', word)
        filtered = re.sub(r'www\S+', '', filtered)
        filtered = re.sub(r'[0-9]\S+', '', filtered)
        filtered = re.sub(r'[^A-Za-z]\S+', '', filtered)
        filtered = re.sub(r'\W+', '', filtered)
        if len(filtered) > 1:
            new_words.append(filtered)

    return new_words

def tokenization(text):
    return nltk.word_tokenize(text)

def count_vectorizer(text):
    return CountVectorizer().build_tokenizer()(text)



def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""

    exclude = set(string.punctuation)

    words = ''.join(ch for ch in words if ch not in exclude)

    return words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english') and word not in stopwords.words('italian') and word not in stopwords.words('french'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def stem_en_words(words):
    stemmer = EnglishStemmer()

    return [stemmer.stem(w) for w in words]

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

