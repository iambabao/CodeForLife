# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/29
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/29
"""

import logging
import numpy as np

from my_utils import init_logger

logger = logging.getLogger(__name__)


def dropout(inputs, keep_rate):
    """

    :param inputs:
    :param keep_rate:
    :return:
    """

    mask = np.random.rand(*inputs.shape) < keep_rate
    outputs = mask * inputs / keep_rate

    return outputs


def main():
    init_logger(logging.INFO)

    arr_in = np.random.rand(3, 4, 5)
    arr_out = dropout(arr_in, keep_rate=0.5)
    logger.info(arr_in)
    logger.info(arr_out)


if __name__ == '__main__':
    main()
