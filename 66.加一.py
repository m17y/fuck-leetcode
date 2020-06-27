#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = int(''.join(map(str,digits)))+1
        print n
        return [int(i) for i in str(n)]
# @lc code=end

