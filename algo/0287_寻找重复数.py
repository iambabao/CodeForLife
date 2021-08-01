# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。

思路：
将下标i到下边num[i]作为一条边，对于一个有重复数字的数组，必定存在两个下标映射到同一个下标，因此会形成环
因此利用快慢指针就可以找到重复的出口，也就是重复的num[i]
注意，最后找结果的时候是先走一步，在判断
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        finder = 0
        while True:
            # 先走一步再判断
            finder = nums[finder]
            slow = nums[slow]
            if slow == finder:
                break

        return slow
