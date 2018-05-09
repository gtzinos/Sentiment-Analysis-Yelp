import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

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
