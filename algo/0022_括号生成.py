# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []

        def backtrack(state, num_left, num_right):
            if len(state) == 2 * n:  # n对括号
                answers.append(''.join(state))
                return
            if num_left < n:  # 左括号少于n个
                state.append('(')
                backtrack(state, num_left + 1, num_right)
                state.pop()
            if num_right < num_left:  # 右括号少于左括号
                state.append(')')
                backtrack(state, num_left, num_right + 1)
                state.pop()

        backtrack([], 0, 0)
        return answers
