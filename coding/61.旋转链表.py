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
        while head and k!=0:
            if head.next:
                newhead.next=head.next
                head = head.next
            else:
                tmp = head
                tmp.next=newhead
                newhead = tmp
                head = newhead
                k-=1
        return newhead


# @lc code=end

