#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        windows = []
        slen = len(s)
        for i in range(slen):
            while s[i] not in t:
                print s[i],t
                windows.pop(0)
                t.remove(t.index(s[i]))
            
            if len(t)==0:
                return windows
        if len(t)!=0:
            return ""
# TODO

# @lc code=end

