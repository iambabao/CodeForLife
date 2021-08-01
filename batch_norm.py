# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/31
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/31
"""

import torch
import torch.nn as nn


class BatchNorm(nn.Module):
    def __init__(self, dimension, eps, momentum=0.1):
        super(BatchNorm, self).__init__()

        self.gamma = nn.Parameter(torch.ones(dimension))
        self.beta = nn.Parameter(torch.zeros(dimension))
        self.eps = eps

        self.momentum = momentum
        self.moving_average_mean = None
        self.moving_average_var = None

    def forward(self, inputs, training=True):
        if training:
            mean = torch.mean(inputs, dim=0, keepdim=True)
            var = torch.var(inputs, dim=0, keepdim=True)
            self.update_moving_average(mean, var)
        else:
            mean = self.moving_average_mean
            var = self.moving_average_var

        return self.gamma * (inputs - mean) / torch.sqrt(var + self.eps) + self.beta

    def update_moving_average(self, mean, var):
        if self.moving_average_mean is None:
            self.moving_average_mean = mean
        else:
            self.moving_average_mean = (1 - self.momentum) * self.moving_average_mean + self.momentum * mean

        if self.moving_average_var is None:
            self.moving_average_var = var
        else:
            self.moving_average_var = (1 - self.momentum) * self.moving_average_var + self.momentum * var
