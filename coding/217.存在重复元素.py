#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 方法二：排序 【通过】
        # 直觉

        # 如果存在重复元素，排序后它们应该相邻。
        l = len(nums)
        # nums.sort()
        numsmap = dict((i,i)for i in nums)
        print len(numsmap)
        return len(nums)>len(numsmap.keys())
        # for i in range(l):

            # 1:
            # if nums[i] in nums[i+1:]: #in 应该是循环判断 时间复杂度太高Time Limit Exceeded
            #     return True
            # 2: 先排序，还是不行时间复杂度还是太高
            # for j in range(i+1,l):
            #     if nums[i]== nums[j]:return True
            #     if nums[j]>nums[i]:break

        # return False
            
# @lc code=end

