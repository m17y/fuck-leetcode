#
# @lc app=leetcode.cn id=349 lang=python
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result
                
        
# @lc code=end

