# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/3
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/3
"""

"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。
"""

import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = [(-val, idx) for idx, val in enumerate(nums[:k])]
        heapq.heapify(pq)

        answer = [-pq[0][0]]
        for i in range(1, len(nums) - k + 1):
            heapq.heappush(pq, (-nums[i + k - 1], i + k - 1))
            while pq[0][1] < i:  # 堆顶元素不在范围内
                heapq.heappop(pq)
            answer.append(-pq[0][0])

        return answer
