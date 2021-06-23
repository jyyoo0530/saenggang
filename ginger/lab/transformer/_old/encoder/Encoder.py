from torch import nn


class Encoder(nn.Module):

    def __init__(self, multi_head_attention, add_norm, feed_forward):
        super(Encoder, self).__init__()
        self.multi_head_attention = multi_head_attention
        self.add_norm = add_norm
        self.feed_forward = feed_forward

    def forward(self, result):
        return result
