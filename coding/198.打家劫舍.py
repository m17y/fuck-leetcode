#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 状态定义：

        # 设动态规划列表 dpdp ，dp[i]dp[i] 代表前 ii 个房子在满足条件下的能偷窃到的最高金额。
        # 转移方程：

        # 设： 有 nn 个房子，前 nn 间能偷窃到的最高金额是 dp[n]dp[n] ，前 n-1n−1 间能偷窃到的最高金额是 dp[n-1]dp[n−1] ，此时向这些房子后加一间房，此房间价值为 numnum ；

        # 加一间房间后： 由于不能抢相邻的房子，意味着抢第 n+1n+1 间就不能抢第 nn 间；那么前 n+1n+1 间房能偷取到的最高金额 dp[n+1]dp[n+1] 一定是以下两种情况的 较大值 ：

        # 不抢第 n+1n+1 个房间，因此等于前 nn 个房子的最高金额，即 dp[n+1] = dp[n]dp[n+1]=dp[n] ；
        # 抢第 n+1n+1 个房间，此时不能抢第 nn 个房间；因此等于前 n-1n−1 个房子的最高金额加上当前房间价值，即 dp[n+1] = dp[n-1] + numdp[n+1]=dp[n−1]+num ；
        # 细心的我们发现： 难道在前 nn 间的最高金额 dp[n]dp[n] 情况下，第 nn 间一定被偷了吗？假设没有被偷，那 n+1n+1 间的最大值应该也可能是 dp[n+1] = dp[n] + numdp[n+1]=dp[n]+num 吧？其实这种假设的情况可以被省略，这是因为：

        # 假设第 nn 间没有被偷，那么此时 dp[n] = dp[n-1]dp[n]=dp[n−1] ，此时 dp[n+1] = dp[n] + num = dp[n-1] + numdp[n+1]=dp[n]+num=dp[n−1]+num ，即两种情况可以 合并为一种情况 考虑；
        # 假设第 nn 间被偷，那么此时 dp[n+1] = dp[n] + numdp[n+1]=dp[n]+num 不可取 ，因为偷了第 nn 间就不能偷第 n+1n+1 间。
        # 最终的转移方程： dp[n+1] = max(dp[n],dp[n-1]+num)dp[n+1]=max(dp[n],dp[n−1]+num)


        l = len(nums)
        if l <=0:return 0
        if l ==1:return nums[0]
        dp = [0 for i in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,l):
            dp[i] =max(dp[i-2]+nums[i],dp[i-1])
        print dp
        return max(dp)
# @lc code=end

