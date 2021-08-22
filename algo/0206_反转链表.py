# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/10
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/10
"""

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev
