#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        dp = [0 for i in prices]
        result = 0
        # for i in range(0,l):
        #     for j in range(i+1,l):
        #         now = prices[j]-prices[i] if (prices[j]-prices[i])>=0 else 0
        #         pre =dp[j-1]
        #         # print dp
        #         # print pre,now,dp[i]
        #         dp[j] = max(pre+now,dp[i])
        # return dp[-1]
        # 两层for 循环 Time Limit Exceeded
        for j in range(1,l):
            now = prices[j]-prices[j-1] if (prices[j]-prices[j-1])>=0 else 0
            pre =dp[j-1]
            # print dp
            # print pre,now,dp[i]
            dp[j] = max(pre+now,dp[j]) 
        print dp
        return dp[-1]
        # TODO 需要做笔记 如何减少循环
# @lc code=end

