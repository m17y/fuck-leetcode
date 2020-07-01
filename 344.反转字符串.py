#
# @lc app=leetcode.cn id=344 lang=python
#
# [344] 反转字符串
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        half = l%2
        for i in range(half):
            s[i],s[l-1-i] = s[l-1-i],s[i]
        return s
# @lc code=end

