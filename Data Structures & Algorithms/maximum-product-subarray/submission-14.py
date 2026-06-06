class Solution:
    def maxProduct(self, nums: List[int]) -> int:       
        pref = nums[0]
        suf = nums[-1]
        res = max(pref, suf)
        
        
        for i in range(1, len(nums)):
            pref = (pref or 1) * nums[i]
            suf = (suf or 1) * nums[len(nums) - i - 1]
            res = max(res, pref, suf)

        return res
        

                

        