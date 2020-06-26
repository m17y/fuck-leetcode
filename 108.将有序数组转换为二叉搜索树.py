#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 题目给出了一个升序排序的有序数组，要求我们转换为一棵高度平衡二叉搜索树。

        # 在此之前，我们先来回忆一下什么是二叉搜索树。
        # 二叉搜索树
        # 二叉搜索树（Binary Search Tree）是指一棵空树或具有如下性质的二叉树：
        # 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值
        # 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值
        # 任意节点的左、右子树也分别为二叉搜索树
        # 没有键值相等的节点
        # 基于以上性质，我们可以得出一个二叉搜索树的特性：二叉搜索树的中序遍历结果为递增序列
        if not nums:
            return None
        mid = len(nums)//2 ##// -> int
        node =  TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid+1:]
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node

        

# @lc code=end

