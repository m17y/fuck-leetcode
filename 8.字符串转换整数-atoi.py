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
        # 手撕代码失败 ！！有限状态机（Finite-state machine, FSM）需要学习
        # if not str:return 0
        # syl = ["+","-","0","1","2",
        # "3","4","5","6","7","8","9"," "
        # ]
        # if str[0] not in syl:return 0
        # result=""
        # pre = 0
        # fh = 0
        # for i in str:
        #     if pre==1:break
        #     if i in syl:
        #         print i,len(result)
        #         if pre==0 and i in (" "):
        #             if len(result)!=0:pre=1
        #         else:
        #             if i =="-" or i=="+":
        #                 fh+=1
        #             if len(result)>0 and (i =="-" or i=="+"):fh+=1
        #             if fh==2:break
        #             result+=i
        #     else:
        #         break
        # print result
        # try:
        #     if int(result)<-2147483648:return -2147483648
        #     print int(result)
        #     if int(result)>=2147483648:return 2147483647
        #     return int(result)
        # except :
        #     return 0
        i=0
        n=len(str)
        while i<n and str[i]==' ':
            i=i+1
        if n==0 or i==n:
            return 0
        flag=1
        if str[i]=='-':
            flag=-1
        if str[i]=='+' or str[i]=='-':
            i=i+1
        INT_MAX=2**31-1
        INT_MIN=-2**31
        ans=0
        while i<n and '0'<=str[i]<='9':
            ans=ans*10+int(str[i])-int('0')
            i+=1
            if(ans-1>INT_MAX):
                break

        ans=ans*flag
        if ans>INT_MAX:
            return INT_MAX
        return INT_MIN if ans<INT_MIN else ans
    
# @lc code=end

