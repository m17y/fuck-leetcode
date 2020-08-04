#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        newhead=head
        while head:
            if !head.next:
                tmp = head
                hexd.next=newhead
                newhead = head
            else:
                newhead.next=head
                head = head.next

# @lc code=end

