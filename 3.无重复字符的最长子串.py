#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 什么是滑动窗口？

        # 其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

        # 如何移动？

        # 我们只要把队列的左边的元素移出就行了，直到满足题目要求！

        # 一直维持这样的队列，找出队列出现最长的长度时候，求出解！

        # if not s:return 0
        # left = 0
        # lookup = set()
        # n = len(s)
        # max_len = 0
        # cur_len = 0
        # for i in range(n):
        #     cur_len += 1
        #     while s[i] in lookup:
        #         lookup.remove(s[left])
        #         left += 1
        #         cur_len -= 1
        #     if cur_len > max_len:max_len = cur_len
        #     lookup.add(s[i])
        # return max_len

        result=[]
        l = len(s)
        for i in range(l):
            

# @lc code=end

