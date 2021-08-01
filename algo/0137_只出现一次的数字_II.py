# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/1
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/1
"""


"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

思路：
对于所有出现三次的数字，其在二进制位上对应出现三个1，因此可以统计每个二进制为出现的次数，不能被3整除说明出现一次的数字对应位为1
注意最高位
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:  # 出现三次的数字其在对应位上也会出现三个1
                # Python 这里对于最高位需要特殊判断，因为输入有正有负，而python 1 << 31是正数
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
