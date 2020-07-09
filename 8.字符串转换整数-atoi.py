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
        if not str:return 0
        syl = ["+","-","0","1","2",
        "3","4","5","6","7","8","9"," "
        ]
        if str[0] not in syl:return 0
        result=""
        for i in str:
            if i in syl:
                if i != " ":
                    result +=i
            else:
                break
        print result
        if result in ["+","-",""]:return 0
        if abs(int(result))>2**32:return -2147483648
        return int(result)
# @lc code=end

