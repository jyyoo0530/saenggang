from torch import nn
import math
import torch
from torch.autograd import Variable
from torchtext.data import get_tokenizer
from ginger.lab.transformer2 import transformer
import itertools

RAW_TEXT = [["I am your father", "je suis ton père"], ["This is my car", "c'est ma voiture"]]

tokenizer = get_tokenizer("spacy", language="en_core_web_sm")


INPUT_TEXT = list(map(lambda x: tokenizer(x), list(map(lambda y: y[0], RAW_TEXT))))
OUTPUT_TEXT = list(map(lambda x: tokenizer(x), list(map(lambda y: y[1], RAW_TEXT))))

WORD_CLOUD = set(sum(INPUT_TEXT,[])+sum(OUTPUT_TEXT,[]))

vocab = {word: i+2 for i, word in enumerate(WORD_CLOUD)}
vocab['<unk>'] = 0
vocab['<pad>'] = 1

d_model = 100
dropout = 0.1

embeddings = transformer.Embeddings(d_model, len(vocab))
pe = transformer.PositionalEncoding(d_model, dropout)

