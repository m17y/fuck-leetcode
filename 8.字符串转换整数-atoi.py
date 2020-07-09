#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        syl = ["+","-","0","1","2"
        "3","4","5","6","7","8","9"
        ]
        if str[0] not in syl:return 0
        
        for i in str:
# @lc code=end

