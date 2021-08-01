# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def b_search(arr, tgt):
            # 去重
            l, r = 0, len(arr) - 1
            while l < r and arr[l] == arr[l + 1]: l += 1
            while l < r and arr[r] == arr[r - 1]: r -= 1
            arr = arr[l:r + 1]

            if len(arr) == 0:
                return False
            if len(arr) == 1:
                return arr[0] == tgt

            mid = len(arr) // 2
            if arr[mid] <= arr[-1]:  # 后半段有序，前半段不一定
                if arr[mid] <= tgt <= arr[-1]:  # 在后半段
                    return b_search(arr[mid:], tgt)
                else:  # 不在后半段
                    return b_search(arr[:mid], tgt)
            else:  # 后半段无序，前半段有序
                if arr[0] <= tgt <= arr[mid - 1]:  # 在前半段
                    return b_search(arr[:mid + 1], tgt)
                else:  # 不在前半段
                    return b_search(arr[mid + 1:], tgt)

        return b_search(nums, target)
