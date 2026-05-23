class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * (len(s)) for _ in range(len(s))]
        max_start = max_offset = float("-inf")

        for offset in range(len(s)):
            for start in range(len(s) - offset):
                if offset == 0:
                    dp[start][start + offset] = True
                elif offset == 1 and s[start] == s[start + offset]:
                    dp[start][start + offset] = True
                elif s[start] == s[start + offset] and dp[start+1][start+offset-1]:
                    dp[start][start + offset] = True
                if dp[start][start + offset] and offset >= max_offset:
                    max_start, max_offset = start, offset
        
        if max_start == float("-inf"):
            return ""
        else:
            return s[max_start:max_start + max_offset + 1]
                    
                    

        