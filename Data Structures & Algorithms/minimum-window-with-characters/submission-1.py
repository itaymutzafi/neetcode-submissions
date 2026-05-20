class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        l = r = 0
        res = ""
        
        if len(s) < len(t):
            return res
        
        while r < len(s):
            if s[r] in counter:
                counter[s[r]] -=1
            while all(val <= 0 for val in counter.values()):
                curr = s[l:r+1]
                res = min(res, curr, key = len) if res else curr
                if s[l] in counter:
                    counter[s[l]] +=1
                l +=1
            r +=1  

        return res

        # "OUZODYXAZV", "XYZ"

        # [OUZOD], [OUZODYX] -> 
        # [ZODYX] -> curr output
        # [ODYX] -> the counter is not 0, continue
        # [ODYXAZ] -> the counter is 0, shrink
        # [YXAZ] -> curr output
        # [XAZ] -> the counter is not 0, continue
        # [XAZV] -> end of the string.
        
        # but if:
        # [XAZVXY] -> the counter is lower than 0, so shrinking
        # [VXY] -> the counter is not 0, continue
        # [VXYZ] -> the counter is 0, shrink
        # so, if the counter is <= 0 for each char, we can shrink. else no.

        

        
        
        
        
        

        
        
