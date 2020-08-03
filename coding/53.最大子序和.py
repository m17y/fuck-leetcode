#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l==0: return 0
        dp = [0 for i in nums]
        dp[0] = nums[0]
        for i in range(1,l):
            print nums[i]
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)
# @lc code=end

