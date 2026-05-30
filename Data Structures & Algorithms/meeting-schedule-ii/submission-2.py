"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # [(25, 579), (218, 918), (1281, 1307), (623, 1320), (685, 1353), (1308, 1358)]
        # [(25, 579), (218, 918), (623, 1320), (685, 1353), (1281, 1307), (1308, 1358)]
        # 1: (25, 579), (623, 1320), 2: (218, 918)
        # need to store the minimum end until now (heap!)

        # 1: (25,579),(623, 1320)
        # 2:(685, 1353)
        # 3:2:(218, 918), (1281, 1307), (1308, 1358)

        
        intervals.sort(key = lambda x: x.start)
        min_end_heap = []
        heapq.heappush(min_end_heap, intervals[0].end)
        
        for i in range(1, len(intervals)):
            if intervals[i].start < min_end_heap[0]:
                heapq.heappush(min_end_heap, intervals[i].end)
            else:
                heapq.heappop(min_end_heap)
                heapq.heappush(min_end_heap, intervals[i].end)
            print(min_end_heap)

        return len(min_end_heap)