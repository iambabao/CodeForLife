# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/3
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/3
"""

"""
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，s1 的排列之一是 s2 的 子串 。
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        golden_counter = [0] * 26
        for token in s1:
            golden_counter[ord(token) - ord('a')] += 1
        cur_counter = [0] * 26
        for token in s2[:len(s1)]:
            cur_counter[ord(token) - ord('a')] += 1

        if cur_counter == golden_counter:
            return True
        for i in range(len(s1), len(s2)):
            cur_counter[ord(s2[i - len(s1)]) - ord('a')] -= 1
            cur_counter[ord(s2[i]) - ord('a')] += 1
            if cur_counter == golden_counter:
                return True

        return False
