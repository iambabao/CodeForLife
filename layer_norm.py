# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/30
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/30
"""

import torch
import torch.nn as nn


class LayerNorm(nn.Module):
    def __init__(self, dimension, eps):
        super(LayerNorm, self).__init__()

        self.gamma = nn.Parameter(torch.ones(dimension))
        self.beta = nn.Parameter(torch.zeros(dimension))
        self.eps = eps

    def forward(self, inputs):
        mean = torch.mean(inputs, dim=-1, keepdim=True)
        var = torch.var(inputs, dim=-1, unbiased=False, keepdim=True)
        return self.gamma * (inputs - mean) / torch.sqrt(var + self.eps) + self.beta
