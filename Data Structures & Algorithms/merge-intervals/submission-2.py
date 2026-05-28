class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        if not intervals:
            return res

        intervals.sort(key = lambda x: x[0]) 
        curr_start, curr_end = intervals[0][0], intervals[0][1]         
        
        # [1,3], [1,5], [6,7]
        # if curr_end <= interval[0], so merge the intervals -> curr_end = interval[1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            print(f"interval is: {interval} curr_end is: {curr_end}")
            if interval[0] <= curr_end:
                curr_end = max(curr_end, interval[1])
            else:
               res.append([curr_start, curr_end])
               curr_start, curr_end = interval[0], interval[1]
            print(f"res is: {res} interval_start is: {curr_start} interval_end is: {curr_end}")
        
        res.append([curr_start, curr_end])
        return res
                
            