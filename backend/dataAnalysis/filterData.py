import numpy as np
import nltk
from nltk.corpus import stopwords, wordnet
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
import string
from nltk.stem.snowball import EnglishStemmer
import unicodedata
from nltk.tokenize import TweetTokenizer
import inflect
import re
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from autocorrect import spell

nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

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

def tokenization(text):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(text)

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
        if word not in stopwords.words('english'):
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

def snowball_stemmer(words):
    """Stem words in list of tokenized words"""
    stemmer = nltk.SnowballStemmer('english')
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def get_pos(word):

    w_synsets = wordnet.synsets(word)

    pos_counts = nltk.Counter()
    pos_counts["n"] = len([item for item in w_synsets if item.pos() == "n"])
    pos_counts["v"] = len([item for item in w_synsets if item.pos() == "v"])
    pos_counts["a"] = len([item for item in w_synsets if item.pos() == "a"])
    pos_counts["r"] = len([item for item in w_synsets if item.pos() == "r"])

    most_common_pos_list = pos_counts.most_common(3)

    return most_common_pos_list[0][0]

def lemmatize_words(words):
    """Stem words in list of tokenized words"""

    lemmatizer = WordNetLemmatizer()
    stems = []
    for word in words:
        stem = lemmatizer.lemmatize(word, get_pos(word))
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

def replace_emoticons(words):
  """Given a dictionary of emoticons, based on https://en.wikipedia.org/wiki/List_of_emoticons
     replace each emoticon to its corresponding word that shows sentiment"""
  emoticons_lexicon = {":-(": "sad_smile", ":(": "sad_smile", ":-|": "sad_smile", ";-(": "sad_smile", ";-<": "sad_smile",
                       "|-{": "sad_smile", ":c": "sad_smile", ":<": "sad_smile", ":‑[": "sad_smile", ">:[": "sad_smile",
                       ">:(": "sad_smile", ":'‑(": "sad_smile", ":'(": "sad_smile", ":-)": "happy_smile", ":)": "happy_smile",
                       ":o)": "happy_smile", ":-}": "happy_smile", ";-}": "happy_smile", ":->": "happy_smile",
                       ";-)": "happy_smile", ":-]": "happy_smile", ":]": "happy_smile", "8-)": "happy_smile", "=]": "happy_smile",
                       "=)": "happy_smile", ":‑D": "happy_smile", "8‑D": "happy_smile", "x‑D": "happy_smile", "X‑D": "happy_smile",
                       ":D": "happy_smile", "8D": "happy_smile", "xD": "happy_smile", "XD": "happy_smile", "=D": "happy_smile",
                       "=3": "happy_smile", "B^D": "happy_smile", ":'‑)": "happy_smile", ":')": "happy_smile"}
  new_words = []
  for word in words:
    new_word = emoticons_lexicon.get(word, word)
    new_words.append(new_word)

  return new_words

def remove_punctuation_preprocess(words):
    """Remove punctuation from list of tokenized words"""

    new_words = []

    for word in words:
      new_word = re.sub(r'[^\w\s]','',word)
      new_words.append(new_word)

    return new_words

def remove_empty_words(words):
    """Remove '' words form a list of words"""

    str_list = list(filter(None, words))

    return str_list

def remove_strip_words(words):
    """Remove ' ' words form a list of words"""

    str_list = list(filter(str.strip, words))

    return str_list

"""Replaces the repeated char sequences people usually type to show emphasis of words
   Example => given a word haaaaaapppyyyyy will become haappyy.
      as we can see, we need to keep some sequences of chars, to show the emphasis, but now
      atleast we have maximum 2 chars for every possible char sequences"""
def replace_emphasis_on_words(words):

    new_words = []

    for word in words:
      new_word = re.sub(r'(.)\1+', r'\1\1', word)
      new_words.append(new_word)

    return new_words

def replace_laughs(words):

    new_words = []

    for word in words:
      new_word = re.sub(r'(.)\1+', r'\1\1', word)
      new_words.append(new_word)

    return new_words

'''replace_negation_words is a method that replaces words that shows negation with 
    the word "not", this will help on constructing more frequent biagrams that will
    correspond better to phrases that shows negation and we will be able to show 
    better and easier the emotion of what the user wanted to say
    
    Example: i cannot wait for the food => (after the whole preprocess becomes) : not wait food
      will be the same with the review : i can't wait for the food, because can't with cannot will both be 
      translated in the word not, and the total frequency of bigram "not wait" will be much higher than the
      two different bigrams "cannot wait" & "can't wait"'''
def replace_negation_words(words):
    negation_lexicon = {"ain't": "is not", "aren't": "are not","can't": "cannot","can't've": "cannot have",
                        "'cause": "because", "could've": "could have","couldn't": "could not",
                        "couldn't've": "could not have","didn't": "did not","doesn't": "does not", "don't": "do not",
                        "hadn't": "had not","hadn't've": "had not have", "hasn't": "has not", "haven't": "have not",
                        "needn't": "need not", "needn't've": "need not have","oughtn't": "ought not",
                        "oughtn't've": "ought not have", "shan't": "shall not","sha'n't": "shall not",
                        "shan't've": "shall not have","shouldn't": "should not","shouldn't've": "should not have",
                        "weren't": "were not","won't": "will not","won't've": "will not have",
                        "wouldn't": "would not","wouldn't've": "would not have",}
    new_words = []

    for word in words:
      new_word = negation_lexicon.get(word, word)
      new_words.append(new_word)

    return new_words

def replace_laugh_sequences(words):
    new_words = []

    for word in words:
      if "xaxa" not in word and "haha" not in word:
        new_words.append(word)
      else:
        new_words.append("laugh")

    return new_words


def replace_slang_internet_words(words):
    slang_lexicon ={"1337":"elite","4":"for","10q":"thanks","10":"excellent","10x":"thanks",
                        "afaik":"as_far_as_i_know","atb":"all_the_best",
                        "b4":"before","bfn":"bye_for_now","btw":"by_the_way",
                        "cu":"see_ya","cya":"see_ya","f9":"fine","ffs":"for_fuck_sake",
                        "fu":"fuck_you","ftw":"for_the_win","ftl":"for_the_loss",
                        "gratz":"congratulations","gtfo":"get_the_fuck_out","gl":"good_luck",
                        "gj":"good_job","gg":"good_job","hf":"have_fun",
                        "idk":"i_dont_know","irl":"in_real_life","jk":"just_kidding",
                        "l8":"late","lmao":"laugh","lmbao":"laugh","lol":"laugh",
                        "n1":"nice_one","nvm":"nevermind","omg":"oh_my_god","omfg":"oh_my_god",
                        "stfu":"shut_it","ty":"thanks","yolo":"you_only_live_once"}
    new_words = []

    for word in words:
      new_word = slang_lexicon.get(word, word)
      new_words.append(new_word)

    return new_words


''' we exclude the word "not" because it shows negation and we need it, especially because this word will help
    on forming meaningful bigrams later '''
def remove_stopwords_with_custom_list(words):
    operators = ['not']

    stop_words = ['ADD HERE THE WORDS YOU WANT TO ALSO REMOVE']  # About 900 stopwords
    nltk_words = list(stopwords.words('english')) # About 150 stopwords
    nltk_words = list(filter(lambda x: x not in operators, nltk_words))

    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in nltk_words and word not in stop_words:
            new_words.append(word)

    return new_words

def spelling_correction(words):

    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        new_words.append(spell(reduce_lengthening(word)))
        # new_words.append(wordCorrection.correction(word))

    return new_words

def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)

def stars_to_label(star):
    """Remove stop words from list of tokenized words"""

    if star <= 3:
      return "negative"
    else :
      return "positive"

def label_to_binary(sentiment):
    """Remove stop words from list of tokenized words"""

    if sentiment == "negative":
      return 0
    else :
      return 1



