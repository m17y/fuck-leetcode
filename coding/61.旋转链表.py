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
        th = head
        l=0
        while th:
            l+=1
            th = th.next
        print l
        index = l-k if (k<l) else l%k
        print index
        pre = head
        while head and index!=0:

            head = head.next
            h = head.next
            index-=1
            if index==0:
                head.next=None

        print pre
        return pre


# @lc code=end

