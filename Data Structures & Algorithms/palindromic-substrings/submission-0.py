class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        
        for offset in range(len(s)):
            for start in range(len(s) - offset):
                end = start + offset
                if offset == 0:
                    dp[start][end] = True
                elif s[start] == s[end]:
                    if offset == 1:
                        dp[start][end] = True
                    elif dp[start + 1][end - 1]:
                        dp[start][end] = True
        
        cnt = 0
        for row in range(len(dp)):
            for col in range(len(dp)):
                cnt += dp[row][col]
        
        return cnt
        
                    
            