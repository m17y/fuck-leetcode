#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1)>len(nums2):
            nums2,nums1 = nums1,nums2
        for i in nums1:
            if i in nums2:
                result.append(i)
        return result
        
# @lc code=end

