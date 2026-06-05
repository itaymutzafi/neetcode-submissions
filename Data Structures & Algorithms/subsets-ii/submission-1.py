class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_list = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(sub_list.copy())
                return
            sub_list.append(nums[i])
            dfs(i+1)
            sub_list.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i +=1
            dfs(i+1)                
        
        dfs(0)
        return res
        