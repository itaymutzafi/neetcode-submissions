import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)
        
        while len(h) > 1:
            first = heapq.heappop(h)
            second = heapq.heappop(h)
            tmp = (-first - (-second))
            heapq.heappush(h, -tmp)
        
        return -h[0] if h else 0
            