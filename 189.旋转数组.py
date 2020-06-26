#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 可以用额外空间保存数组
        
        # 思路一：插入

        # 思路二：拼接

        # 思路三：三个翻转 ， 整体翻转， 前k翻转，后k翻转

        # 思路四：模拟过程
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums

# @lc code=end

