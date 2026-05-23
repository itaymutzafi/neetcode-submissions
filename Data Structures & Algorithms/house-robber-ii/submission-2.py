class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_with_first = [0 for _ in range(len(nums) + 1)]
        dp_with_last = [0 for _ in range(len(nums) + 1)]
        
        dp_with_first[1] = nums[0]
        
        for i in range(2, len(nums) + 1):
            if i != len(nums):
                dp_with_first[i] = max(dp_with_first[i-1], dp_with_first[i-2] + nums[i-1])
            else:
                dp_with_first[i] = dp_with_first[i-1]
            dp_with_last[i] = max(dp_with_last[i-1], dp_with_last[i-2] + nums[i-1])
        
        return max(dp_with_first[-1], dp_with_last[-1])