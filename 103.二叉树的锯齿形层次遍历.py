#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 解题思路 1.层次遍历 2.当层数为奇数时需要templist 需要将tmplist的数据反转一下
        # 和层次遍历二叉树 多出来一步：-》
        ############################ 当层数为奇数时需要templist 需要将tmplist的数据反转一下
        if not root:return []
        result=[[root.val]]
        queue = [root.left,root.right]
        pre=1 #偶数从左往右 奇数从右往左
        while queue:
            tmplist = []
            lqueue = len(queue)
            for i in range(lqueue):
                if queue[i]:
                    tmplist.append(queue[i].val)
                    queue.append(queue[i].left)
                    queue.append(queue[i].right)
            if pre%2!=0:
                tmplist = tmplist[::-1]

            pre+=1
            result.append(tmplist)
            queue = queue[lqueue:]
        return result[:-1]
            


            
# @lc code=end

