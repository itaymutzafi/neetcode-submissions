class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        window = Counter()
        formed = 0
        l = r = 0
        res = ""
        
        if len(s) < len(t):
            return res
        
        while r < len(s):
            ch = s[r]
            window[ch] +=1
            if ch in counter:
                if window[ch] == counter[ch]:
                    formed +=1

            while formed == len(counter):
                curr = s[l:r+1]
                res = min(res, curr, key = len) if res else curr
                window[s[l]] -=1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    formed -=1
                l +=1
            r +=1  

        return res

        

        
        
        
        
        

        
        
