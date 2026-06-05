class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # this is not just to take or not to take words. this is also how many I want to take
        # c X
        # ca X
        # cat ! -> sincars -> sin! -> cars -> s -> X 
        d = {}
        res = s
        
        def helper(s):
            if not s:
                return False
            if s in d:
                return d[s]
            if s in wordDict:
                d[s] = True
                return True
            for i in range(1, len(s)):
                if helper(s[:i]) and helper(s[i:]):
                    d[s] = True
                    return True
            d[s] = False
            return False

        return helper(s)
                    
                
            
        
        
        