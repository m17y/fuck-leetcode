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
        if k==0 or head==None or l==1 or k%l==0: return head

        index = l-k if (k<l) else l-k%l


        print index
        oldpre = head
        newpre = None
        while head and index!=0:
            index-=1
            if index==0:
                newpre = head.next
                head.next=None
            head = head.next

        print newpre,oldpre

        tmpnewpre = newpre

        while tmpnewpre:
            if tmpnewpre.next==None:
                tmpnewpre.next = oldpre
                break
            tmpnewpre = tmpnewpre.next

        print newpre
        return newpre


# @lc code=end

