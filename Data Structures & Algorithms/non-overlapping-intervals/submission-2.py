class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:
            return res

        intervals.sort(key = lambda x : (x[0], x[1]))
        curr_start, curr_end = intervals[0][0], intervals[0][1]
                
        print(intervals)
        for i in range(1, len(intervals)):
            if curr_end > intervals[i][0]:
                print(f"curr end is: {curr_end}, intervals[i][0] is: {intervals[i][0]}")
                res +=1
                if curr_end > intervals[i][1]:
                    curr_start, curr_end = intervals[i][0], intervals[i][1]
            else:
                curr_start, curr_end = intervals[i][0], intervals[i][1]
        
        return res
            
        
        
        # [1,3], [1,4], [2,4]
        # [1,2], [1,3], [1,4], [2,4]

        # 1 2 3 4
        # -----
        # -------
        #   ---

        # each time you need to "merge", so give up of this.
        # we want to take the narrow edges in each time
        # so if I sort by left side, and then for second prioriy the right edge, I will get this
        
