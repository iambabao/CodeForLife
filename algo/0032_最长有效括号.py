# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/8
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/8
"""

"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0

        answer = 0
        dp = [0] * (len(s) + 1)  # dp[i]为以第i个token为结尾的有效括号长度，dp[0]特例
        for i in range(2, len(s) + 1):  # 从第2个token开始
            if s[i - 1] == ')':  # 必须以）为结尾
                if s[i - 2] == '(':  # 前一个token为（，直接和前一个token匹配
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 2 >= 0 and s[i - dp[i - 1] - 2] == '(':  # 前一个token为），再往前回溯dp[i - 1] + 1个token匹配
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                answer = max(answer, dp[i])

        return answer
