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
        pre =None
        l2head = l2
        while l1:
            tmp1 = l1.next
            while l2:
                tmp2 = l2.next
                if l1.val<l2.val:
                    l2.next = l1
                    l2.next.next = tmp
                if l2.next==None:
                    l2.next = l1
                l2 = tmp2  
            l1 = tmp1
        return l2

                    

                    

        while 
            


        
# @lc code=end

