# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/9/2
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/9/2
"""

"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        minr, minc, maxr, maxc = 0, 0, len(matrix), len(matrix[0])

        results = []
        while minr < maxr and minc < maxc:
            for i in range(minc, maxc):
                results.append(matrix[minr][i])
            for i in range(minr + 1, maxr):
                results.append(matrix[i][maxc - 1])
            # 至少剩两行
            if minr + 1 != maxr:
                for i in range(maxc - 2, minc - 1, -1):
                    results.append(matrix[maxr - 1][i])
            # 至少剩两列
            if minc + 1 != maxc:
                for i in range(maxr - 2, minr, -1):
                    results.append(matrix[i][minc])
            minr += 1
            minc += 1
            maxr -= 1
            maxc -= 1

        return results
