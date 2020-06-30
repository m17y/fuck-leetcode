#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                if i>j:
                    nums[i],nums[j] = nums[j],nums[i]
                    
                    

        
# @lc code=end

