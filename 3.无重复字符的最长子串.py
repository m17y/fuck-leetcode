#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 1
        index = 0
        childl = []
        for i in range(1,l):
            if s[i] not in childl:
                childl.append(s[i])
                l +=1
            else:
                childl = [s[i]]
                dp[i] = max(dp[i-1],dp[i]+1)
        
        return dp[-1]
# @lc code=end

