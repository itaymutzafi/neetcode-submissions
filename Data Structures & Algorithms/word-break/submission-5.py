class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        res = s
        d = {}
        
        def helper(i):
            if i >= len(s):
                return True
            if i in d:
                return d[i]
            res = False
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words:
                    res = helper(j) or res
            d[i] = res
            return res

        return helper(0)

                    
                
            
        
        
        