class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        sub_list = []

        def dfs(i):
            if i >= len(nums):
                return
            sub_list.append(nums[i])
            tmp_sorted = sorted(sub_list)
            if tmp_sorted not in res:
                res.append(tmp_sorted.copy())
            dfs(i+1)
            sub_list.pop()
            dfs(i+1)
        
        dfs(0)
        return res
        