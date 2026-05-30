class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,2],[2,4],[1,4]]
        # כל מה שאני רוצה לדעת, זה אם ההתחלה של האינטרוול הנוכחי היא בתוך אינטרוול קיים
        
        res = 0

        if not intervals:
            return res

        intervals.sort(key = lambda x : x[1])
        curr_end = float("-inf")
        
        for interval in intervals:
            if interval[0] >= curr_end:
                curr_end = interval[1]
            else:
                res +=1
        
        return res
        