# from torch import nn
#
# inputs = "I am your father"
#
#
# def get_vocab(corpus):
#     word_set = set(corpus.split())
#     vocab = {tkn: i + 2 for i, tkn in enumerate(word_set)}
#     vocab['<unk>'] = 0
#     vocab['<pad>'] = 1
#     return vocab
#
#
# vocab = get_vocab(inputs)
#
# embedding_layer = nn.Embedding(num_embeddings=len(vocab), embedding_dim=3, padding_idx=1)

from torch import nn
from torchtext.vocab import GloVe
from torchtext.vocab import Vectors
from torchtext.legacy import data, datasets


TEXT = data.Field(sequential=True, batch_first=True, lower=True)
LABEL = data.Field(sequential=False, batch_first=True)
trainset, testset = datasets.IMDB.splits(TEXT, LABEL)
TEXT.build_vocab(trainset, vectors=GloVe(name='6B', dim=50), max_size=10000, min_freq=10)
LABEL.build_vocab(trainset)

embedding_layer = nn.Embedding.from_pretrained(TEXT.vocab.vectors, freeze=False)