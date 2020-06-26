#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #递归
        pre = 0
        def ts(left,right):
            if left>=right:return left

            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
            print left ,right
            return ts(left,right)
        return ts(1,n)
        #迭代
        l, r= 1,n
        while l<r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        
        return l



        
# @lc code=end

if __name__ == '__main__':
    
    