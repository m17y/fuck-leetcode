#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(first = 0,vis=[]):
            # 所有数都填完了
            print first
            if first ==n-1:  
                res.append(nums[:])#[:] deepCopy
            for i in range(0, n):
                if(vis[i]==0):
                    vis[i] = 1
                    nums[first] = i
                    # 继续递归填下一个数
                    dfs(first + 1,vis)
                    # 撤销操作
                    vis[i] = 0
                
        vis=[0 for i in nums]
        vis.append(0)
        n = len(nums)
        res = []
        dfs(0,vis)
        return res

# @lc code=end

