# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

思路：
现将负数置为n + 1，然后将对应下标的数置为负数，没被置为负数的即为缺失的数
注意0
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 将非正数置为 n + 1
        for i, value in enumerate(nums):
            if value <= 0:
                nums[i] = n + 1

        # 为所有元素打标记，将对应位置置为负数
        for value in nums:
            abs_value = abs(value)
            if abs_value <= n:
                nums[abs_value - 1] = -abs(nums[abs_value - 1])

        # 找到没被置为负数的位置
        for i, value in enumerate(nums):
            if value > 0:
                return i + 1

        return n + 1
