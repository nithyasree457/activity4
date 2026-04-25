class Solution:
    def rob(self, nums):
        def rob_line(arr):
            prev1 = 0
            prev2 = 0
            for num in arr:
                prev1, prev2 = max(prev1, prev2 + num), prev1
            return prev1
        
        if len(nums) == 1:
            return nums[0]
        
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
