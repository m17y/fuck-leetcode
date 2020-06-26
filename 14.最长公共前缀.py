#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if bool(strs)==False:return ""
        if len(strs)==1:return strs[0]
        fstr = strs[0]
        fl = len(fstr)
        commonstr = ""
        for i in range(1):
            for j in range(1,fl+1):
                tmpstr = fstr[i:j]
                tmpbool = []
                for istr in strs[1:]:
                    if len(istr)<j:tmpbool.append(False)
                    tmpbool.append(bool(tmpstr==istr[i:j]))
                if False not in tmpbool:
                    if len(tmpstr)>len(commonstr):
                        commonstr=tmpstr
                
        return commonstr

# @lc code=end

