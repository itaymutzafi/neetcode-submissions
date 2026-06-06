class Solution:
    def maxProduct(self, nums: List[int]) -> int:       
        pref = [num for num in nums]
        suf = [num for num in nums]
        res = max(pref[0], suf[-1])
        
        
        for i in range(1, len(nums)):
            pref[i] = (pref[i-1] or 1) * nums[i]
            suf[len(nums) - i - 1] = (suf[len(nums) - i] or 1) * nums[len(nums) - i -1]
            res = max(res, pref[i], suf[len(nums) - i - 1])

        return res
        

                

        