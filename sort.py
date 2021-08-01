# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/31
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/31
"""


def partition(arr, left, right):
    key = arr[left]
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
    arr[left] = key
    return left


def quick_sort(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        index = partition(arr, left, right)
        quick_sort(arr[:index])
        quick_sort(arr[index + 1:])


