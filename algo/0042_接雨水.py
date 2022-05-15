# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/9/2
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/9/2
"""

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 1：记录左右两端最高的点
        # left, right = [0] * len(height), [0] * len(height)
        # left[0] = height[0]
        # right[-1] = height[-1]
        #
        # for i in range(1, len(height)):
        #     left[i] = max(left[i - 1], height[i])
        # for i in range(len(height) - 2, -1, -1):
        #     right[i] = max(right[i + 1], height[i])
        #
        # ans = 0
        # for i in range(len(height)):
        #     ans += min(left[i], right[i]) - height[i]
        #
        # return ans

        # 2：填平
        ans = 0
        stack = []

        # 把低洼处填平
        for i, h in enumerate(height):
            # 当前位置比栈顶元素高
            while len(stack) > 0 and h > height[stack[-1]]:
                first = stack.pop()
                if len(stack) == 0:  # 加上当前位置至少宽度为三才能填
                    break
                second = stack[-1]
                curr_w = i - second - 1
                curr_h = min(height[i], height[second]) - height[first]
                ans += curr_w * curr_h
            stack.append(i)

        return ans
