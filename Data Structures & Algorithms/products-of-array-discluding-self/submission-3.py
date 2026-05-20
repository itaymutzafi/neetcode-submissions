class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        # init
        pref[0] = suff[n-1] = 1

        # calculate pref:
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        
        # calculate suff:
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        # calculate res:
        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]
        
        return res
        

            
        
            
        