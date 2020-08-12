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
        # TODO xk
        origin=ListNode(0)
        a=0
        pre = origin
        ll1=self.len(l1)
        ll2=self.len(l2)
        if l11<ll2:
            l1,l2=l2,l1
        while l1 and a!=0:
            print l1.val,l2.val
            if l1.val+l2.val+a>=10:
                origin.next = ListNode(l1.val+l2.val+a-10)
                a=1
            else:
                origin.next = ListNode(l1.val+l2.val+a)
                a=0
            l1 = l1.next
            l2 = l2.next
            origin = origin.next
        if a==1:
            origin.next = ListNode(1)  

        return pre.next
            
        
# @lc code=end

