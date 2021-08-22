# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/10
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/10
"""

"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        new_head = ListNode(next=head)

        prev = new_head  # prev记录子链表前一个节点
        start = new_head.next
        while start is not None:
            # 确保剩余链表长度
            end = start
            for _ in range(k - 1):
                end = end.next
                if end is None:
                    return new_head.next
            next = end.next  # next记录子链表后一个节点

            start, end = process(start, end)  # 翻转子链表

            # 重新拼接子链表
            prev.next = start
            end.next = next
            prev, start = end, end.next

        return new_head.next


def process(start, end):
    prev = start
    curr = prev.next
    while prev != end:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return end, start
