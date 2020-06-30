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
        for i in range(9):
            line = filter(lambda x:x!=".",board[i])
            if sum(line) != sum(set(line)):
                return False
            cl
            

# @lc code=end

