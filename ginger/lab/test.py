import numpy as np
import torch
from glob import glob
from os.path import join
import pandas as pd

dir_base = '/home/jyyoo/PycharmProjects/nlp'
extension = '/localdata/test'
path = dir_base + extension
output = glob(join(path, "**"))

raw = open(output[0]).read()
raw = raw.split('\n')
raw.pop(-1)
raw.pop(0)
raw = list(map(lambda x: x.split(','), raw))

df = pd.DataFrame(raw, columns=['date', 'idx'])
df['input'] = df['idx']
df['output'] = df['idx'].shift(-1)
df = df.replace('.', np.nan)
df = df.ffill()
df = df.drop('idx', axis=1)
df = df.astype({'input': 'float', 'output': 'float'})
df['input'] = df['input'] / 10000
df['output'] = df['output'] / 10000
