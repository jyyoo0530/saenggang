import math

import torch


def pos_encoding(d_model, max_len=5000):
    pe = torch.zeros(max_len, d_model)
    pos = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp((-math.log(10000) / d_model) * torch.arange(0, d_model, 2).float())

    pe[:, 0::2] = torch.sin(pos * div_term)
    pe[:, 1::2] = torch.cos(pos * div_term)
    # pe = pe.unsqueeze(0).transpose(0, 1)

    return pe.data
