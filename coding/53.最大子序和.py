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
        ma = nums[0]
        for i in range(1,l):
                ma = max(ma+nums[i],ma)
        return ma
# @lc code=end

