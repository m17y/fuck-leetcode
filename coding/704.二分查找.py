#
# @lc app=leetcode.cn id=704 lang=python
#
# [704] 二分查找
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums)-1
        while left<=right:
            half = left+(right-left)//2
            if nums[half]>target:
                right = half-1
            elif nums[half]==target:
                return half
            else:
                left = half+1
        return -1

# @lc code=end

