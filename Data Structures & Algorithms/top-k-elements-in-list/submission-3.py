from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        h = []
        for num, cnt in counter.items():
            heapq.heappush(h, (cnt, num))        
            if len(h) > k:
                heapq.heappop(h)
        res = []
        for cnt, num in h:
            res.append(num)

        return res
        