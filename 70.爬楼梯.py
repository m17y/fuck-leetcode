#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(x)=f(x−1)+f(x−2)
        if n==1:return 1
        if n==2:return 2
        return climbStairs(n-1)+climbStairs(n-2)

# @lc code=end

