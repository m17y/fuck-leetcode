#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        l = len(nums)
        for i in range(l):
            for j in (i+1,l):
                c = 0-(i+j)
                if c<j:break
                if c in nums[j:]:
                    result.append([i,j,c])
        return result
# @lc code=end

