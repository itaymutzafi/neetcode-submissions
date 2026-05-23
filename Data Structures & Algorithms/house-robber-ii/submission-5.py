class Solution:
    def rob(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums: List[int]) -> int:
            prevprev, prev = 0, nums[0]

            # for each house, rob the current house, or take the prev one

            for i in range(1, len(nums)):
                rob = max(prevprev + nums[i], prev)
                prevprev = prev
                prev = rob
            print(nums)
            print(prev)
            
            return prev
        
        return max(helper(nums[:-1]), helper(nums[1:]))
