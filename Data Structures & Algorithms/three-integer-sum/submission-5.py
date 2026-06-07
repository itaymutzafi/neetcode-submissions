class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # one + two + three == 0
        # it means that every (one + two) == Three
        # so I can do in O(n^2), for each

        # # [-1,0,1,2,-1,-4]
        # # [-4,-1,-1,0,1,2]
        # # why sorting? in order to have a progress that I continue with just bigger nums.
        # # and also if I checked one num, I can pass the other nums that equal to it after (has to not contain dups)
        
        # -4 can take whatever it wants from -4 1->len(nums)
        # and then check if -4 + -1 == -5?
        # if -5 in the dic? and if so, if -5 index is bigger than first and second? if so, enter.

        nums.sort()
        d = {-nums[i]: i for i in range(len(nums))}
        res = []


        for i in range(len(nums)):
            first = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                second = nums[j]
                third = first + second
                if third in d and d[third] > j:
                    res.append([first, second, -third])
        
        return res
                
        
        
        