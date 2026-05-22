class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums = list(set(nums))
        nums.sort()


        def helper(curr_sum, L, j):
            if target < curr_sum:
                return
            if target == curr_sum:
                self.res.append(L.copy())
                return 
            for i in range(j, len(nums)):
                L.append(nums[i])
                helper(curr_sum + nums[i], L, i)
                L.pop()
        
        tmp = []
        helper(0, tmp, 0)
        return self.res
            
            