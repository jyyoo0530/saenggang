from torch import nn


class ScaledDotProductionAttention(nn.Module):

    def __init__(self, matmul, softmax, mask, scale):
        super(ScaledDotProductionAttention, self).__init__()
        self.matmul = matmul
        self.softmax = softmax
        self.mask = mask
        self.scale = scale

    def compute_attention(self, query, key, value):
        "Scaled Dot-Production Attention"
        key_d = query.size(-1)


    def forward(self, result):
        return result
