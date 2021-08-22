# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/8
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/8
"""

"""
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。
"""


from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        remove_left, remove_right = 0, 0
        for ch in s:
            if ch == '(':
                remove_left += 1
            elif ch == ')':
                if remove_left > 0:
                    remove_left -= 1
                else:
                    remove_right += 1

        answers = set()

        def search(index, count_l, count_r, remove_l, remove_r, state):
            if index == len(s):
                if remove_l == 0 and remove_r == 0:
                    answers.add(''.join(state))
                return

            # 删除当前的token
            if s[index] == '(' and remove_l > 0:
                search(index + 1, count_l, count_r, remove_l - 1, remove_r, state)
            if s[index] == ')' and remove_r > 0:
                search(index + 1, count_l, count_r, remove_l, remove_r - 1, state)

            # 保留当前token
            state.append(s[index])
            if s[index] != '(' and s[index] != ')':  # 非括号
                search(index + 1, count_l, count_r, remove_l, remove_r, state)
            elif s[index] == '(':  # 左括号，可以直接加入state
                search(index + 1, count_l + 1, count_r, remove_l, remove_r, state)
            elif s[index] == ')' and count_r < count_l:  # 又括号，仅在右括号数量少于左括号时加入state
                search(index + 1, count_l, count_r + 1, remove_l, remove_r, state)
            state.pop()

        search(0, 0, 0, remove_left, remove_right, [])
        return list(answers)
