#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#

# @lc code=start
class Solution(object):
    def xx(self,num,dividend, divisor):
        divisor+divisor
        if (dividend-(divisor+divisor))>divisor:
            return num+num,dividend-(divisor+divisor),divisor
        else:
            return num,dividend,divisor

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        z = 1
        r = 0
        while dividend>divisor:
            dividend = dividend-divisor
            r=r+z
            z,dividend,divisor = self.xx(z,dividend,divisor)
            dividend,divisor = dividend,divisor
            if z!=z:
                r=r+z
        return r

# @lc code=end

