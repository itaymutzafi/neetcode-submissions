class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_window = 0
        seen = set()
        
        for r in range(len(s)):
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l +=1
            
            seen.add(s[r])
            max_window = max(max_window, len(seen))
        
        return max_window
                
            