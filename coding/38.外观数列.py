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
        m=["",""]
        for i in range(2,n+1):
            for j in str(result):
                if j!=m[0]:
                    str(result)+str(m[1])+str(m[0])
                else:
                    m[1] += 1

        return str(result)
        # @lc code=end

