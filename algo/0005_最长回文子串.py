# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/9/2
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/9/2
"""

"""
给你一个字符串 s，找到 s 中最长的回文子串。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        begin = 0
        max_len = 1
        # 先枚举子串长度
        for length in range(2, len(s) + 1):
            # 枚举左边界
            for i in range(len(s)):
                j = i + length - 1
                if j >= len(s):
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and length > max_len:
                    begin = i
                    max_len = length
        return s[begin:begin + max_len]
