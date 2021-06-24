from glob import glob
from os.path import join
import spacy
from gensim.parsing.preprocessing import remove_stopwords
import nltk
from functools import reduce
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import datetime

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


def get_file_list(dir_extention):
    dir_base = '/home/jyyoo/PycharmProjects/nlp'
    path = dir_base + dir_extention
    output = glob(join(path, "**"))
    return output


def preprocess(file, separator='.', steps="*"):
    target = open(file).read()
    ##문장 분리
    target = target.replace("<br />", "")
    target = target.split(separator)
    if steps == "*":
        ## AA. Text Normalization
        # 1) 대소문자 변경
        target = list(map(lambda x: x.lower(), target))
        # 2) 숫자제거
        import re
        target = list(map(lambda x: re.sub(r'\d+', '', x), target))
        # 3) 문장부호 제거
        import string
        target = list(map(lambda x: x.translate(str.maketrans("", "", string.punctuation)), target))
        # 4) whitespace 제거
        target = list(map(lambda x: x.strip(), target))
        target = list(filter(None, target))

        ## BB. Tokenization
        # 1) stop_word 제거
        target = list(map(lambda x: remove_stopwords(x), target))

        ### 단어 토큰화
        target = list(map(lambda x: word_tokenize(x), target))

        # 2) stemming ( books -> book, looked -> look )
        stemmer = PorterStemmer()
        target = list(map(lambda x: list(map(lambda y: stemmer.stem(y), x)), target))

        # 3) lemmatization
        lemmatizer = WordNetLemmatizer()
        target = list(map(lambda x: list(map(lambda y: lemmatizer.lemmatize(y), x)), target))

        # 4) finalization
        word_set = list(map(lambda x: set(x), target))

        ### 단어 결합
        # target = list(map(lambda x: ' '.join(x), target))

        # # 4) POS(Part of Speech Tagging, 품사와 태깅)
        # from textblob import TextBlob
        #
        # # 5) Chunking (shallow parsing)
        # reg_exp = "NP: {<DT>?<JJ>*<NN>}"
        # rp = nltk.RegexpParser(reg_exp)
        # target = list(map(lambda x: list(map(lambda y: rp.parse(y), x)), target))
        print(datetime.datetime.now())

    return target

