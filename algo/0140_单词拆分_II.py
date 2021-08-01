# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""

"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

思路：
基于回溯
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}

        def backtrack(index):
            """
            返回s[index:]所有可能的划分

            :param index:
            :return:
            """
            if index in cache: return cache[index]  # 利用cache加速

            if index == len(s):
                cache[index] = [[]]
                return [[]]

            results = []
            for i in range(index + 1, len(s) + 1):  # s[index:i]作为一个单词，s[i:]递归调用
                cur_word = s[index:i]
                if cur_word in wordDict:
                    breaks = backtrack(i)
                    for cur_break in breaks:
                        results.append([cur_word] + cur_break.copy())  # 注意copy
            cache[index] = results
            return results

        all_splits = backtrack(0)
        return [' '.join(words) for words in all_splits]
