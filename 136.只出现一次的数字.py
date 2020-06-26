#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序后 判断此数和前后是否相等
        # 补充 异或牛逼
        # https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
        nums.sort()
        p = nums[0]
        nums.insert(0,None)
        nums.append(None)
        l = len(nums)
        c = 1
        for i in range(1,l-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
        return None
                    

# @lc code=end

