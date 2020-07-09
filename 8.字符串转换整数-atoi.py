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
        pre = 0
        for i in str:
            print len(result)
            if pre==1:break
            if i in syl:
                print i,len(result)
                if pre==0 and i==" ":
                    if len(result)!=0:pre=1
                else:
                    result+=i
            else:
                break
        print result
        try:
            if int(result)>2147483648:return -2147483648
            return int(result)
        except :
            return 0
        
# @lc code=end

