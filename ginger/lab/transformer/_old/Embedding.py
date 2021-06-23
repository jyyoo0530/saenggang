import math

from torch import nn


class Embedding(nn.Module):

    def __init__(self, counts_vocab, d_model):
        super(Embedding, self).__init__()
        self.embedding = nn.Embedding(counts_vocab, d_model)
        self.d_model = d_model

    def forward(self, x):
        return self.embedding(x) * math.sqrt(self.d_model)
