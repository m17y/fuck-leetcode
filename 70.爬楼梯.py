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
        # 递归 时间复杂度会很高
        # if n==1:return 1
        # if n==2:return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        dp =[1,2]
        for i in range(2,n):
            print i,dp[i-1]+dp[i-2]
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
# @lc code=end

