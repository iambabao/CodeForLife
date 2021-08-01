# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""


"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def b_search(arr):
            # 去重
            l, r = 0, len(arr) - 1
            while l < r and arr[l] == arr[l + 1]: l += 1
            while l < r and arr[r] == arr[r - 1]: r -= 1
            arr = arr[l:r + 1]

            if len(arr) == 0:
                return 1e6
            if len(arr) == 1:
                return arr[0]

            mid = len(arr) // 2
            if arr[mid] <= arr[-1]:  # 后半段有序，前半段不一定
                return min(arr[mid], b_search(arr[:mid]))
            else:  # 后半段无序，前半段有序
                return min(arr[0], b_search(arr[mid + 1:]))

        return b_search(nums)
