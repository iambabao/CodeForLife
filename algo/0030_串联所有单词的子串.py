# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/3
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/3
"""

"""
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
"""

from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s is None or len(words) == 0:
            return []

        answer = []
        word_len = len(words[0])
        total_len = word_len * len(words)
        golden_counter = Counter(words)
        for i in range(len(s) - total_len + 1):  # 从i开始的子串
            cur_counter = Counter()
            for j in range(i, i + total_len, word_len):  # 取对应个数的span
                cur_counter[s[j:j + word_len]] += 1
            if cur_counter == golden_counter:
                answer.append(i)
        return answer
