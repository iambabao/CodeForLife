# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/31
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/31
"""


def lower_bound(arr, val):
    """
    第一个大于等于val的数

    :param arr:
    :param val:
    :return:
    """
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < val:
            l = mid + 1
        else:
            r = mid
    return l


def upper_bound(arr, val):
    """
    第一个大于val的数

    :param arr:
    :param val:
    :return:
    """
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= val:
            l = mid + 1
        else:
            r = mid
    return l


def main():
    arr = [1, 1, 1, 2, 2, 2, 4, 4, 4]
    print(1, lower_bound(arr, 1))
    print(1, upper_bound(arr, 1))
    print(3, lower_bound(arr, 3))
    print(3, upper_bound(arr, 3))
    print(4, lower_bound(arr, 4))
    print(4, upper_bound(arr, 4))


if __name__ == '__main__':
    main()
