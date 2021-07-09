from glob import glob
from os.path import join
import pandas as pd
from torch import nn
import torch
import nltk
import itertools

# 1) 데이터 프로세스에 탑재

dir_base = '/home/jyyoo/PycharmProjects/nlp'
extension = '/localdata/test'
path = dir_base + extension
output = glob(join(path, "**"))

raw = open(output[0], encoding='latin-1').read()
raw = raw.split('\n')
raw.pop(-1)
raw = list(map(lambda x: x[1:-1], raw))
raw = list(map(lambda x: x.split('","'), raw))
output_raw = list(map(lambda x: x[0], raw))
input_raw = list(map(lambda x: x[-1], raw))


# df = pd.DataFrame(raw, columns=['sentiment', 'idx', 'date', 'query', 'user', 'content'])
# train_input = df['content']
# train_output = df['sentiment']
# train_output = train_output.astype('float')

# 2) 임베딩을 위한 전처리

# 3) word tokenizing
from nltk.tokenize import word_tokenize

tokenizer = word_tokenize
input_raw = list(map(lambda x: tokenizer(x, language='english'), input_raw))


def find_longest(corpus):
    x = 0
    for i in corpus:
        y = len(i)
        if x < y:
            x = y
        else:
            continue
    return x

longest = find_longest(input_raw)

corpus = itertools.chain(*input_raw)
corpus = set(corpus)

# 4) nn.Embedding()
embedding_dim = 50
embedding = nn.Embedding(len(corpus), embedding_dim)

# 5)