from torch import nn


class MultiHeadAttention(nn.Module):

    def __init__(self, scaled_dot_production_attention):
        super(MultiHeadAttention, self).__init__()
        self.scaled_dot_production_attention = scaled_dot_production_attention

    def forward(self, result):
        return result
