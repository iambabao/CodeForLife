# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/3
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/3
"""

"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = 0
        summ = 0
        ptr1, ptr2 = 0, 0
        while ptr2 < len(nums):
            while summ < target and ptr2 < len(nums):
                summ += nums[ptr2]
                ptr2 += 1

            while summ >= target and ptr1 < ptr2:
                if answer == 0 or ptr2 - ptr1 < answer:
                    answer = ptr2 - ptr1
                summ -= nums[ptr1]
                ptr1 += 1

        return answer
