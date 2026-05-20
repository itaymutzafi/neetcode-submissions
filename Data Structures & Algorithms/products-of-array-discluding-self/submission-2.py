class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = [0 for _ in range(len(nums))]
        zeros_cnt = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_cnt +=1                          

        if zeros_cnt > 1:
            return dp
        
        # zeros_cnt <= 1
        
        zero_i = None
        product = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_i = i
            else:
                product *= nums[i]
        
        if zeros_cnt == 1:
            dp[zero_i] = product
            return dp
        
        else: # zero_cnt is 0
            for i in range(len(nums)):
                dp[i] = product // nums[i]
            return dp
            
        