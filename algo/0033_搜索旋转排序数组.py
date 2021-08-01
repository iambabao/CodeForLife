# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

思路：
二分查找，必有一段是有序的
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def b_search(arr, tgt, k):
            if len(arr) == 0:
                return -1
            elif len(arr) == 1:
                return k if arr[0] == tgt else -1

            mid = len(arr) // 2
            if arr[mid] <= arr[-1]:  # 后半段有序，前半段不一定
                if arr[mid] <= tgt <= arr[-1]:
                    return b_search(arr[mid:], tgt, k + mid)
                else:
                    return b_search(arr[:mid], tgt, k)
            else:  # 后半段无序，前半段有序
                if arr[0] <= tgt <= arr[mid]:
                    return b_search(arr[:mid + 1], tgt, k)
                else:
                    return b_search(arr[mid + 1:], tgt, k + mid + 1)

        return b_search(nums, target, 0)
