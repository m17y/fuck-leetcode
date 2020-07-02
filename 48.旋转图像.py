#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix[0])        
        # # transpose matrix
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # # reverse each row
        # for i in range(n):
        #     matrix[i].reverse()
        # @lc code=end

