class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = {num : i for i, num in enumerate(nums)}
        res = []
        
        for i in range(len(nums)):
            first = nums[i]
            if i > 0 and first == nums[i-1]:
                continue # avoid duplicates
            for j in range(i + 1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                second = nums[j]
                third = -(first + second)
                if third in d and d[third] > j and d[third] > i:
                    res.append([first, second, -(first + second)])
        return res
                
        