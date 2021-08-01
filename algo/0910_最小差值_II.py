# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
给你一个整数数组 A，对于每个整数 A[i]，可以选择 x = -K 或是 x = K （K 总是非负整数），并将 x 加到 A[i] 中。

在此过程之后，得到数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

思路：
找到一个中间点，之前的全部都+k，之后的全部-k
"""

from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        minn, maxx = nums[0], nums[-1]
        answer = maxx - minn
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            answer = min(answer, max(maxx - k, a + k) - min(minn + k, b - k))  # 小的数字+k，大的数字-k

        return answer
