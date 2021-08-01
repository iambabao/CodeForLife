# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

import torch
import torch.nn as nn


def mean_square_error(labels, logits):
    loss = torch.sqrt((logits - labels)**2)
    return torch.mean(loss, dim=0)


class LinearRegression(nn.Module):
    def __init__(self, hidden_size):
        super(LinearRegression, self).__init__()

        self.w = nn.Parameter(torch.rand(hidden_size))
        self.b = nn.Parameter(torch.rand(1))

    def forward(self, inputs):
        """

        :param inputs: (batch_size, hidden_size)
        :return:
        """
        logits = torch.sigmoid(torch.matmul(inputs, self.w) + self.b)

        return logits

    def train_step(self, inputs, labels, lr=1e-3):
        """

        :param inputs: (batch_size, hidden_size)
        :param labels: (batch_size,)
        :param lr:
        :return:
        """
        logits = self.forward(inputs)  # (batch_size,)

        loss = mean_square_error(labels, logits)

        gradient_w = torch.mean(inputs * (logits - labels), dim=0)  # (hidden_size)
        self.w = self.w - lr * gradient_w
        gradient_b = torch.mean(logits - labels, dim=0)  # (hidden_size)
        self.b = self.b - lr * gradient_b

        return loss
