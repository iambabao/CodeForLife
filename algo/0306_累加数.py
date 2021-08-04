# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/4
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/4
"""

"""
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

思路：
先确定first number和second number，然后向后搜索，后面的序列可以根绝前两个数字的和确定
注意：
前导零的处理
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(first, second, index):
            while index < len(num):
                summ = str(int(first) + int(second))  # 因为保证不存在0作为前导，所以可以取str(summ)
                if index + len(summ) > len(num) or num[index:index + len(summ)] != summ:
                    return False
                index += len(summ)
                first = second
                second = summ
            return True

        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                first_num = num[:i]
                second_num = num[i:j]
                if dfs(first_num, second_num, j):
                    return True
                # 0只能单独成为一个数字，所以second_num以0为开始时，只用判断j = i + 1的情况，然后直接break
                if num[i] == '0':
                    break
            # 同理，first_num以0为开始时，只用判断i = 1的情况，然后直接break
            if num[0] == '0':
                break

        return False
