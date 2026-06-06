import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = [] # smallest numbers, max is the median
        self.min_heap = [] # biggest numbers, min is the median

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return
        elif num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) - len(self.min_heap) > 1:
            tmp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, tmp)
            return
        if len(self.min_heap) - len(self.max_heap) > 1:
            tmp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -tmp)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        