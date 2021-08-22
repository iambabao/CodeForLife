# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/5
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/5
"""

"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def search(index, current):
            if index == len(nums):
                answers.append(current.copy())
                return

            for i in range(len(nums)):
                # 对同一个位置填入两次一样的数会造成重复，所以只保留第一个i
                if visited[i] or (i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]):
                    continue

                current.append(nums[i])
                visited[i] = True
                search(index + 1, current)
                visited[i] = False
                current.pop()

        answers = []
        visited = [False] * len(nums)
        nums = sorted(nums)  # 需要先排序，才能保证不填入重复数
        search(0, [])

        return answers
