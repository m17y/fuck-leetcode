#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def treelength(root):
            if root is None:
                return 0,False
            l,bl = treelength(root.left)
            r,bl = treelength(root.right)
            return max(l,r)+1,bool(l>r)
        result = []
        stock=[]
        pre = root
        mapl = {}
        pleft = 0
        pright = 0
        t,bl = treelength(root)
        print t,bl
        while root or stock:
            if root:
                stock.append(root)
                root = root.left
            else:
                index = len(stock)
                print index,stock
                p = stock.pop()
                mapl.setdefault(index,[p.val])
                mapl[index].append(p.val)
                if p.right!=None:
                    mapl[index].append(p.right.val)


# @lc code=end

