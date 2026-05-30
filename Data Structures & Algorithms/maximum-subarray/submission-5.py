class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # #nums=[5,4,-1,7,8] 
        # curr_sum = 5, 9, 8, 15, 23! :-)
        # for each i, expand the sum? or start new one? -> dp[i] = max(dp[i-1] + nums[i], nums[i])

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
        
            