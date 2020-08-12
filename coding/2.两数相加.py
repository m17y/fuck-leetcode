#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        origin=ListNode(0)

        while l1 and l2:
            origin.next = ListNode(l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next
            origin = origin.next
        return origin.next
            
        
# @lc code=end

