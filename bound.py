# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/31
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/31
"""


def lower_bound(arr, val):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= val:
            r = mid
        else:
            l = mid + 1
    return l


def upper_bound(arr, val):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > val:
            r = mid
        else:
            l = mid + 1
    return l
