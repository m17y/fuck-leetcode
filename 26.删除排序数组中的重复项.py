#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[index]:
                index += 1
                nums[index]=nums[i]
        print index   
        return len(nums[:index+1])

# @lc code=end

