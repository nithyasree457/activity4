class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        
        if (total + target) % 2 != 0 or total < abs(target):
            return 0
        
        subset = (total + target) // 2
        
        dp = [0] * (subset + 1)
        dp[0] = 1
        
        for num in nums:
            for j in range(subset, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset]
