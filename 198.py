class Solution:
    def rob(self, nums):
        prev1 = 0
        prev2 = 0
        
        for num in nums:
            prev1, prev2 = max(prev1, prev2 + num), prev1
        
        return prev1
