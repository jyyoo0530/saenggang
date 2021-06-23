import numpy as np
import pandas as pd
import torch
import transformers as ppb
from more_itertools import padded
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://github.com/clairett/pytorch-sentiment-classification/raw/master/data/SST2/train.tsv',
                 delimiter='\t', header=None)
content = df.iloc[:, 0]
marked_content = list(map(lambda x: "[CLS]" + x + "[SEP]", content))
print(len(marked_content))

model_id = 'bert-base-multilingual-cased'
model = ppb.Bert.from_pretrained(model_id)
tokenizer = ppb.BertTokenizer.from_pretrained(model_id)

