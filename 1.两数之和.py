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
        
        l = len(target):
        for i in range(l):
            d = nums - nums[i]
            if d in mums[i+1:]:
                return [i,nums.index(d)]
        return []
# @lc code=end

