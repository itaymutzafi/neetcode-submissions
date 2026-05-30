class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,0,1,0]
        # [True,True,False,True,True]

        # [1,2,1,0,1]
        # [False,False,False,False,True]
        
        dp = [False for _ in range(len(nums))]
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for step in range(nums[i] + 1):
                if i + step < len(nums) and dp[i+step]:
                    dp[i] = True
        
        return dp[0]
            
            