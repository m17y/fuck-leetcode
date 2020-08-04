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
    def length(self,head): #计算链表长度
        num = 0;
        node = head;
        while node:
            num+=1
            node = node.next
        return num
    # def rotateRight(self, head, k):
    #     """
    #     :type head: ListNode
    #     :type k: int
    #     :rtype: ListNode
    #     """
    #     th = head
    #     l=self.length(head)

    #     if k==0 or head==None or l==1 or k%l==0: return head

    #     index = l-k if (k<l) else l-k%l


    #     print index
    #     oldpre = head
    #     newpre = None
    #     while head and index!=0:
    #         index-=1
    #         if index==0:
    #             newpre = head.next
    #             head.next=None
    #         head = head.next

    #     print newpre,oldpre

    #     tmpnewpre = newpre

    #     while tmpnewpre:
    #         if tmpnewpre.next==None:
    #             tmpnewpre.next = oldpre
    #             break
    #         tmpnewpre = tmpnewpre.next

    #     print newpre
    #     return newpre
 
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        fast = slow = head #建立快慢指针
        if self.length(head)==0:
            return head
        leng = k%self.length(head)
        for i in range(leng):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        #核心
        print head
        print fast,slow
        fast.next = head
        print head.val
        head = slow.next
        print head.val
        slow.next = None
        # print head
        return head

# @lc code=end

