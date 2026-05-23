class Solution:
    def numDecodings(self, s: str) -> int:
        # "1210"
        # "1" -> one valid, base case
        # "12" -> I can take 1 but I can not take one. so I add one option to every option that has in i-1, and if I take i-1 I add one more option to each that was in i-2
        
        if not s:
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1

        for i in range(len(s)):
            if s[i] != "0": # we can add one more option, while don't take the one before
                dp[i + 1] += dp[i]
            if i > 0 and 10 <= int(s[i-1] + s[i]) <= 26: # we can add one more option, while take the one before
                dp[i + 1] += dp[i-1]
        
        return dp[-1]
        