class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums.sort()

        def helper(curr_sum, L, j):
            if target < curr_sum:
                return
            if target == curr_sum:
                self.res.append(L.copy())
            for i in range(j, len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                L.append(nums[i])
                helper(curr_sum + nums[i], L, i)
                L.pop()
        
        tmp = []
        helper(0, tmp, 0)
        return self.res
            
            