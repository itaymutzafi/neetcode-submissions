class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        longest = 0
        
        for num in nums:
            curr = 1
            if num - 1 not in d:
                tmp = num + 1
                while tmp in d:
                    curr += 1
                    tmp +=1
            longest = max(longest, curr)
        
        return longest
                    
        
        

