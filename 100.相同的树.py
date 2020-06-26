#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        a=[]
        zz = []
        def pr(z):
            if z==None:a.append("null")
            if z:
                a.append(z.val)
                pr(z.left)
                pr(z.right)
        pr(p)
        zz=a
        print a
        a=[]
        pr(q)
        print a,zz
        return bool(a==zz)
# @lc code=end

