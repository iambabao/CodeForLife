# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/3
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/3
"""

"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remain = 0  # 剩余的token总数
        counter = {}  # 每个token剩余的数量
        for ch in t:
            remain += 1
            counter[ch] = counter.get(ch, 0) + 1

        ans = ''
        ptr1, ptr2 = 0, 0
        while ptr2 < len(s):
            while remain > 0 and ptr2 < len(s):
                if s[ptr2] in counter:  # 消耗对应的token
                    counter[s[ptr2]] -= 1
                    if counter[s[ptr2]] >= 0:
                        remain -= 1
                ptr2 += 1

            while remain == 0 and ptr1 < ptr2:  # 缩小答案
                if ans == '' or (ans != '' and ptr2 - ptr1 < len(ans)):
                    ans = s[ptr1:ptr2]
                if s[ptr1] in counter:  # 放回对应token
                    counter[s[ptr1]] += 1
                    if counter[s[ptr1]] > 0:
                        remain += 1
                ptr1 += 1
        return ans
