#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=[]
        status = False
        while head:
            if head in a: 
                status = True 
                break
            a.append(head)
            head=head.next

        return status

        # 快慢指针 66666
        slow = head
        fast = head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                return False
            if slow == fast:
                return True
        return False

    
        
        
# @lc code=end

