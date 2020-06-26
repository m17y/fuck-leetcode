#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # ol1 = len(nums1)
        # pindex = 0
        # for num2 in nums2:
        #     l1 = len(nums1)
        #     for i in range(pindex,l1-1):
        #         if num2>=nums1[i] and nums1[i+1]>num2:
        #             nums1.insert(i+1,num2)
        #             pindex = i+2
        #             break
        #         elif nums1[i]==0:
        #             nums1.insert(i,num2)
        #             pindex = i+1
        #             break
        # z = nums1[:ol1]  
        # return z
        j = 0
        print m
        for i in xrange(m,m+n):
            nums1[i] = nums2[j]
            j += 1
        nums1.sort()



# @lc code=end

