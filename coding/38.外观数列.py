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
            m={}
            for j in str(result):
                print j,m.keys()
                if j not in m.keys():
                    for k,v in m.items():
                        str(result)+str(v)+k
                    m={}
                m.setdefault(j,0)
                m[j] += 1

        return str(result)
        # @lc code=end

