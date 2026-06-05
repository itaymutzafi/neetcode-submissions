class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  "XYYX" -> just one character
        
        # X -> {X: 1}
        #   Y -> {X:1, Y: 1}
        #   Y -> {X:1, Y: 2} len == 3 - max = 1 so valid
        #   X -> {X:2, Y: 2} len = 4, len - max = 2 = k so valid. so this is the max

        d = {}
        max_len = most_freq = 0
        l, r = 0,0
        
        
        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1
            most_freq = max(most_freq, d[s[r]])
            while r - l + 1 - most_freq > k:
                d[s[l]] -=1
                most_freq = max(d.values())
                l +=1
            max_len = max(max_len, r - l + 1)
            r +=1
        
        return max_len
                
                