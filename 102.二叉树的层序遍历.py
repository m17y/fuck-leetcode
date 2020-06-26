#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return [] 
        result=[]
        queue = [root]
        while queue:
            templ = []
            lqueue = len(queue)
            for i in range(lqueue):
                templ.append(queue[i].val)
                if queue[i].left :queue.append(queue[i].left)
                if queue[i].right :queue.append(queue[i].right)
            queue = queue[lqueue:]
            result.append(templ)
        return result

# @lc code=end

