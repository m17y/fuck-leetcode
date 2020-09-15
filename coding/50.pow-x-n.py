#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def quickMul(N):
            ans = 1.0
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                N = N//2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

# @lc code=end

