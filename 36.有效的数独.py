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
        # 应该是官方一次迭代方法 
        # 但是line = filter(lambda x:x!=".",board[i]) 这一步其实可以用额外空间优化
        cl = [[],[],[],[],[],[],[],[],[]]
        pl = [[[],[],[]],[[],[],[]],[[],[],[]]] #3*3宫内只能出现一次
        for i in range(9):
            line = filter(lambda x:x!=".",board[i])
            if len(line) != len(set(line)):
                return False
            for no,j in enumerate(board[i]):
                if j!=".":
                    print j,cl[no]
                    if j in cl[no]:
                        return False
                    else:
                        cl[no].append(j)
                    if j in pl[i/3][no/3]:
                        return False
                    else:
                        pl[i/3][no/3].append(j)
        return True
            

            

# @lc code=end

