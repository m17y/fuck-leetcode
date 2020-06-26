#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a=[]
        def helper(root):
            if root:
                helper(root.left)
                a.append(root.val)
                helper(root.right)
        helper(root)
        itera=[]
        # return a
        def iter(root):
            #中序遍历：左根右
            result = []
            stock = []
            if root==None:
                return result
            while root or stock:
                if root:
                    stock.append(root)
                    root = root.left
                else:
                    p = stock.pop()
                    result.append(p.val)
                    if p.right!=None:
                        root = p.right
            return result
        
        return iter(root)
#迭代方法解题思路 基于栈的遍历：先便利完所有的 左树 然后一次回退到上一个子树去判断有没有 右树
# @lc code=end

