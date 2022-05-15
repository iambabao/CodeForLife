# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/9/2
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/9/2
"""

"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        ans = 0

        while start < end:
            ans = max(ans, min(height[start], height[end]) * (end - start))
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return ans
