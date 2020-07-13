#
# @lc app=leetcode.cn id=876 lang=python
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow
# @lc code=end

