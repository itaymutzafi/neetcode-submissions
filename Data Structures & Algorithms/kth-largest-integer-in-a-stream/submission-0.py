import heapq
class KthLargest:   
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.capacity = k
        for i in range(len(nums)):
            heapq.heappush(self.h, nums[i])
            if len(self.h) > self.capacity:
                heapq.heappop(self.h)       

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.capacity:
            heapq.heappop(self.h)
        return self.h[0]
        
