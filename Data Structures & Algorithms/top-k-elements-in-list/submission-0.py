class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = sorted(nums, key = nums.count, reverse = True)
        
        res = set()
        i = 0
        
        while len(res) < k and i < len(L):
            res.add(L[i])
            i +=1

        return list(res)
        