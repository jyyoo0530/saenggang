import torch.nn as nn
from bert.tokenization.bert_tokenization import FullTokenizer

corpus = ['I am your father',
          'I am your mother',
          'This is an apple',
          'This is a banana']

tokenizer = FullTokenizer(corpus)
