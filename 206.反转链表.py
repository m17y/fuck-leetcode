#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(None)
        tmp.next = head
        pre = tmp
        while tmp.next!=None:
            _tmp = tmp.next
            tmp.next = pre
            tmp = 

            temp,tmp.next = temp.next,temp
            pre = tmp

# @lc code=end

