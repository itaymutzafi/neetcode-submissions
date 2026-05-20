class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        max_window = 0
        
        while left < len(s):
            seen = set()
            curr_window = 0
            right = left

            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                curr_window +=1
                right +=1
            
            max_window = max(max_window, curr_window)
            left +=1
        
        return max_window
                
            