import math
from glob import glob
from os.path import join

import pandas as pd
from gensim.parsing.preprocessing import remove_stopwords
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import datetime
from gensim.models import FastText, word2vec
from gensim import utils
from sklearn.manifold import TSNE
import matplotlib as mpl
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from torchtext.legacy import data, datasets
from torchtext.legacy.data import TabularDataset
from torchtext.legacy.data import Iterator

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


def get_file_list(dir_extension):
    dir_base = '/home/jyyoo/PycharmProjects/nlp'
    path = dir_base + dir_extension
    output = glob(join(path, "**"))
    return output


def tokenize_custom(file, separator='.', steps="*"):
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


def tokenize_tools(file):
    output = list(utils.tokenize(file))
    print(datetime.datetime.now())
    return output


def embedding(corpus, model_type):
    if model_type == "fasttext":
        model = FastText(workers=10)
    if model_type == "word2vec":
        model = word2vec.Word2Vec(workers=10)
    model.build_vocab(corpus)
    model.train(corpus, total_examples=len(corpus), epochs=10)
    return model


def visualization(model):
    ## data 생성부
    mpl.rcParams['axes.unicode_minus'] = False
    vocab = model.wv.index_to_key
    X = model.wv[vocab]
    tsne = TSNE(n_components=3)

    X_tsne = tsne.fit_transform(X[:100, :])
    df = pd.DataFrame(X_tsne, index=vocab[:100], columns=['x', 'y'])
    df.shape
    df.head(10)
    fig = plt.figure()
    fig.set_size_inches(40, 20)
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(df['x'], df['y'])

    for word, pos in df.iterrows():
        ax.annotate(word, pos, fontsize=30)
    plt.show()


def test(file_list):
    sentences = list(map(lambda x: list(sent_tokenize(open(x).read())), file_list))
    train_set = sentences[:math.floor(len(sentences) / 2)]
    test_set = sentences[math.floor(len(sentences) / 2):]
    train_data = pd.DataFrame()
    test_data = pd.DataFrame()
    for i in train_set:
        train_data = pd.concat([train_data, pd.DataFrame(i)])
    for j in test_set:
        test_data = pd.concat([test_data, pd.DataFrame(j)])

    train_data.to_csv("train_data.csv", index=False)
    test_data.to_csv("test_data.csv", index=False)

    TEXT = data.Field(sequential=True,
                      use_vocab=True,
                      tokenize=word_tokenize,
                      lower=True,
                      batch_first=True
                      )
    LABEL = data.Field(sequential=False,
                       use_vocab=False,
                       batch_first=False,
                       is_target=True)

    train_data, test_data = TabularDataset.splits(
        path='.', train='train_data.csv', test='test_data.csv', format='csv',
        fields=[('text', TEXT), ('label', LABEL)], skip_header=True)

    batch_size = 5
    train_loader = Iterator(dataset=train_data, batch_size=batch_size)
    test_loader = Iterator(dataset=test_data, batch_size=batch_size)
