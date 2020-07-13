#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #解题思路 Tag：二叉树层次遍历，队列，反转数组
        result=[]
        queue = [root]
        while queue:
            templ = []
            lqueue = len(queue)
            for i in range(lqueue):
                if queue[i]:
                    templ.append(queue[i].val)
                    queue.append(queue[i].left)
                    queue.append(queue[i].right)
                else:
                    templ.append("null")
            queue = queue[lqueue:]
            if not bool(templ==templ[::-1]):
                return False
            result.append(templ)

        print result
        return True

# @lc code=end

