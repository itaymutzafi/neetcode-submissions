class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:       
        # [(0, 7)]
        # [(1, 1)] -> I am lower than the stack higher, so I pop it, and do ((i- 0) * heights[0])
        # [(1,1)] -> [(7,2), (1,1)]
        # 2 is lower than 7, so pop 7 and then (3-2) * 7 = 7
        # [(2,3), (1,1)]
        # [(2,4),(1,1)]
        # [(4,5),(2,4),(1,1)]
        # (4,5) -> ((5-4) + (5-5)) * 4
        # (2,4) -> ((5-4) + (4-1)) * 2
        # (1,1) -> ((5-1) + (1-0)) * 1 = 5
        
        if len(heights) == 1:
            return heights[0]

        q = []
        res = 0

        for i in range(len(heights)):
            while q and heights[q[-1]] >= heights[i]:
                j = q.pop()
                left = q[-1] if q else -1
                print(f"i is {i} l is {left} j is {j} heights[j] is {heights[j]}")
                res = max(res, heights[j] * (i - j - 1 + (j - left)))
            
            q.append(i)
        
        print(q)
        
        while q:
            i = q.pop()
            j = q[-1] if q else -1
            curr = ((i - j) + (len(heights) -1 - i)) * heights[i]
            res = max(res, curr)
        
        return res
        
        

        
        
        