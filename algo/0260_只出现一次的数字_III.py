# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

思路：
所有数字异或之后，两个不同的数字比会产生二进制上的1，找到对应位置后，就可以将所有数字划分成两个部分分别异或，各自留下一个数字
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = 0
        for val in nums:
            result ^= val

        # 找到为1的一位下标，index = 100...00
        index = 1
        while index & result == 0:
            index <<= 1

        # 分组亦或
        val_a, val_b = 0, 0
        for val in nums:
            if val & index != 0:  # 对应位为1，结果不为0
                val_a ^= val
            else:  # 对应位为0，结果为0
                val_b ^= val

        return [val_a, val_b]
