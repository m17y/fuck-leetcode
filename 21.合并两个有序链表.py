#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # prehead = ListNode(-1)
        # prev = prehead
        # while l1:
        #     tmp1 = l1.next
        #     tmp22 = l2
        #     while l2:
        #         tmp2 = l2.next
        #         if l1.val<=l2.val:
        #             l1.next = None
        #             l2.next = l1
        #             prev.next = l2
        #             prev = prev.next
        #         l2 = tmp2
        #     if not l2:
        #         l1.next = None
        #         prev.next = l1
        #         prev = prev.next
        #     l1 = tmp1
        # return prehead.next
   
# @lc code=end

