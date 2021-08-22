# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/10
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/10
"""

"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(0, head)
        slow, fast = new_head, new_head
        for _ in range(n):
            fast = fast.next

        prev = None  # slow的前一个节点
        while fast is not None:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next  # 删除第n个阶段

        return new_head.next
