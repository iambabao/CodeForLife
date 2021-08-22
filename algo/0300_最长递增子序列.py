# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/3
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/3
"""

"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for val in nums:
            index = lower_bound(dp, val)  # 严格上升
            # index = upper_bound(dp, val)  # 非严格上升
            if index == len(dp):
                dp.append(val)
            else:
                dp[index] = val
        return len(dp)


# 第一个大于等于val的位置
def lower_bound(arr, val):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left


# 第一个大于val的位置
def upper_bound(arr, val):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= val:
            left = mid + 1
        else:
            right = mid
    return left
