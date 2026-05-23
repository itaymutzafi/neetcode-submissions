class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp = [[False] * (len(s)) for _ in range(len(s))]
        max_start = max_offset = 0

        for offset in range(len(s)):
            for start in range(len(s) - offset):
                end = start + offset
                if offset == 0:
                    dp[start][end] = True
                elif offset == 1 and s[start] == s[end]:
                    dp[start][end] = True
                elif s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = True
                if dp[start][end] and offset >= max_offset:
                    max_start, max_offset = start, offset
    
        return s[max_start:max_start + max_offset + 1]
                    
                    

        