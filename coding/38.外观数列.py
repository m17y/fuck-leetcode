#
# @lc app=leetcode.cn id=38 lang=python
#
# [38] 外观数列
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = 1
        for i in range(2,n+1):
            result = i
        # @lc code=end

