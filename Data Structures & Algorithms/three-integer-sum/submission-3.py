from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            counter[nums[i]] -=1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                counter[nums[j]] -=1
                
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                
                target = -(nums[j] + nums[i])
                if counter[target] > 0:
                    res.append([nums[j], nums[i], target])
            for j in range(i+1, len(nums)):
                counter[nums[j]] +=1
        
        return res
            
            