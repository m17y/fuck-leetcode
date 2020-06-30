#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = len(nums)
        for i in range(l):
            d = target - nums[i]
            if d in nums[i+1:]:
                return [i,nums[i+1:].index(d)+i+1]
        return []
# @lc code=end

