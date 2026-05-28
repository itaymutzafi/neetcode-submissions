import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)
        
        while l <= r:
            mid  = (r + l) // 2
            curr_h = 0
            
            for pile in piles:
                curr_h += math.ceil(pile / mid)

            if curr_h <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

        # maybe binary search for k.
        # the range is from 1 to max_pile. 
        
        
        
        
        
        
        