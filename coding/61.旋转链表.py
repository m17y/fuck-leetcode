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
        if k==0 or head==None: return head
        th = head
        l=0
        while th:
            l+=1
            th = th.next
        print l
        index = l-k if (k<l) else l-k%l
        print index
        pre = head
        newpre = None
        while head and index!=0:

            newpre = head.next
            index-=1
            if index==0:
                head.next=None
            head = head.next

        print newpre,pre
        tpre = newpre
        while newpre:
            tmp = newpre
            newpre = newpre.next
            if tmp.next==None:
                tmp.next = pre
        print tpre
        return tpre


# @lc code=end

