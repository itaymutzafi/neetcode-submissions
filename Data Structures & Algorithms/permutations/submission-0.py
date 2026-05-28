class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def rec(L):
            if len(L) == n:
                res.append(L.copy())
                return
            
            for j in range(n):
                curr = nums[j]
                if curr not in visited:
                    L.append(curr)
                    visited.add(curr)
                    rec(L)
                    L.pop()
                    visited.remove(curr)
        L = []
        visited = set()
        rec(L)
        return res
