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
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


# @lc code=end

