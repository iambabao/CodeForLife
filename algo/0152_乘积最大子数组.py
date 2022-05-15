# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/9/2
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/9/2
"""

"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        maxx, minn = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_maxx = max(nums[i], minn * nums[i], maxx * nums[i])
            cur_minn = min(nums[i], minn * nums[i], maxx * nums[i])
            # 连续子数组
            maxx = cur_maxx
            minn = cur_minn
            ans = max(ans, maxx)

        return ans
