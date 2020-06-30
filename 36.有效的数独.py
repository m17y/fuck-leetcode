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

        for i in range(9):
            sum(i) = sum(set(i))

# @lc code=end

