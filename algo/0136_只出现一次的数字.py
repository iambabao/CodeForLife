# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

思路：
利用异或运算的特性
0 ^ val = val
val ^ val = 0
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            res ^= val
        return res
