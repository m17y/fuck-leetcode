#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cl = [[],[],[],[],[],[],[],[],[]]
        pl = [[],[],[],[],[],[],[],[],[]] #3*3宫内只能出现一次
        for i in range(9):
            line = filter(lambda x:x!=".",board[i])
            if sum(line) != sum(set(line)):
                return False
            for no,j in enumerate(board[i]):
                if j in cl[j]:
                    return False
                else:
                    cl[j].append(j)
                if i%3
            

            

# @lc code=end

