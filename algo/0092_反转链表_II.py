# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/8/10
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/8/10
"""

"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        new_head = ListNode(next=head)

        # 找到left前一个位置
        curr = new_head
        for _ in range(left - 1):
            curr = curr.next

        temp_head = curr.next
        temp_prev = curr.next
        temp_curr = temp_prev.next
        for _ in range(right - left):
            temp_next = temp_curr.next
            temp_curr.next = temp_prev
            temp_prev = temp_curr
            temp_curr = temp_next

        curr.next = temp_prev
        temp_head.next = temp_curr

        return new_head.next
