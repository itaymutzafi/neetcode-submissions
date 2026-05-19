from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        return sorted(counter.keys(), key = lambda x: counter[x], reverse = True)[:k]
        