#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 因为二叉搜索树中序遍历是递增的,所以我们可以中序遍历判断前一数是否小于后一个数.
        stack = []
        status = True
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            print root.val
            if pre and root.val<= pre.val:
                return False
            pre = root
            root = root.right
        return True


            # if root:
            #     if root.left!=None:
            #         status = bool(root.left.val<root.val)
            #         if status==False:return status
            #     stock.append(root)
            #     root = root.left
            # else:
            #     p = stock.pop()
            #     if p.right!=None:
            #         print ("right",status,p.right.val,p.val)
            #         status = bool(p.right.val>p.val)
            #         if status==False:return status
            #         root = p.right
            #         print root, stock
        return status

                

# @lc code=end

