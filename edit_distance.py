# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/31
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/31
"""

def edit_distance(tokens_1, tokens_2):
    dp = [[0] * (len(tokens_2) + 1) for _ in range(len(tokens_1) + 1)]

    for i in range(len(tokens_1) + 1):
        dp[i][0] = i
    for i in range(len(tokens_2) + 1):
        dp[0][i] = i

    for i in range(1, len(tokens_1) + 1):
        for j in range(1, len(tokens_2) + 1):
            if tokens_1[i - 1] == tokens_2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1  # insert or delete
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)  # replace

    return dp[-1][-1]
