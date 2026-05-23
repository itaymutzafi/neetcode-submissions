class Solution:
    def rob(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(start, end) -> int:
            prevprev, prev = 0, nums[start]

            # for each house, rob the current house, or take the prev one
            print(f"start i is: {start}, end i is: {end}")
            for i in range(start + 1, end):
                rob = max(prevprev + nums[i], prev)
                prevprev = prev
                prev = rob
                print(f"rob is {rob}, i is: {i}")
            
            return prev
        
        return max(helper(0, len(nums)-1), helper(1, len(nums)))
