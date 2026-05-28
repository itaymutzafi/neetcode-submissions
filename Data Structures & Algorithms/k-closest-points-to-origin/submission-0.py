import heapq

class Solution:
    def euclide_dis(self, point: List[int]):
        return (point[0] * point[0] + point[1] * point[1]) ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        
        for point in points:
            heapq.heappush(h, (-self.euclide_dis(point), point[0], point[1]))
            if len(h) > k:
                heapq.heappop(h)
        
        return [[point[1], point[2]] for point in h] 
