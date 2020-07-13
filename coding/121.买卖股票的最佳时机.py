#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        result = 0
        _min = prices[0]
        _max = prices[0]
        l = len(prices)
        for i in range(1,l):
            if prices[i]<_min:_min = prices[i]
            print _min,prices[i]-_min
            result = max(result,prices[i]-_min)
        return result

# @lc code=end

