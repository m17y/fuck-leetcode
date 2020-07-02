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
        # 第一种 先转置 在反转数据
        # n = len(matrix[0])        
        # # transpose matrix
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # # reverse each row
        # for i in range(n):
        #     matrix[i].reverse()
        # 第二种 对角互换 逐步内部收缩 可以扩展成任何多维数组的旋转
        pos1,pos2 = 0,len(matrix)-1

        while   pos1<pos2:
            add = 0
            while   add < pos2-pos1:
                #左上角为0块，右上角为1块，右下角为2块，左下角为3块
                temp = matrix[pos2-add][pos1]
                matrix[pos2-add][pos1] = matrix[pos2][pos2-add]
                #3 = 2
                matrix[pos2][pos2-add] = matrix[pos1+add][pos2]
                #2 = 1
                matrix[pos1+add][pos2] = matrix[pos1][pos1+add]
                #1 = 0
                matrix[pos1][pos1+add] = temp
                #0 = temp
                add = add+1
            pos1 = pos1+1
            pos2 = pos2-1
        return matrix
        # 变形 每一个环向前移位4怎么做？？？
        # TODO
        # @lc code=end

