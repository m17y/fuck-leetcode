#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nn = 0
        temp = head
        while temp is not None:
            temp = temp.next
            nn+=1
        print nn
        temp = head
        while temp is not None:
            if nn==n:
                temp.next=temp.next.next
                temp.val = temp.next.val
                break
            else:
                n-=1
                temp = temp.next
        print head
        return head
        # node_no = 0
        # node = head
        # while node is not None:
        #     node = node.next
        #     node_no += 1
        # node_no -= n + 1

        # node = head
        # if node_no == -1:
        #     head = head.next
        # else:
        #     while(node_no):
        #         node = node.next
        #         node_no -= 1
        #     node.next = node.next.next
        # return head
# @lc code=end

