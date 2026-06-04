class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:              
        res = []
        subset = []
        
        def helper(j):
            if j >= len(nums):
                res.append(subset.copy())
                return
            # choose nums[j]
            subset.append(nums[j])
            # conitnue with nums[j] in the subset, while just those after can be inserted.
            helper(j+1)
            
            # don't choose nums[j]
            subset.pop()
            helper(j+1)

        helper(0)
        return res


        
                
                
        
        # always insert [] first

        # []
        # [1]
        # [1,2] [1,3]
        # [1,2,3]
        
        # [2]
        # [2,3]
        
        # [3]

        # each i - not_used is just nums[i:]
        
        
        
        
        
