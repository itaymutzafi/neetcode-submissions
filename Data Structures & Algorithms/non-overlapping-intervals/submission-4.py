class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:
            return res

        intervals.sort(key = lambda x : (x[0], x[1]))
        curr_start, curr_end = intervals[0][0], intervals[0][1]
                
        for i in range(1, len(intervals)):
            if curr_end > intervals[i][0]:
                res +=1
                if curr_end > intervals[i][1]:
                    curr_start, curr_end = intervals[i][0], intervals[i][1]
            else:
                curr_start, curr_end = intervals[i][0], intervals[i][1]
        
        return res       
