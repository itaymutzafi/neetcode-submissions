from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        if not s:
            return max_len
        l = r = 0     
        counter = defaultdict(int)
        max_freq = 0
        
        while r < len(s):
            counter[s[r]] +=1
            max_freq = max(max_freq, counter[s[r]])
            
            while r - l + 1 - max_freq > k:
                counter[s[l]] -=1
                l +=1

            max_len = max(max_len, r - l + 1)
            r +=1
        
        return max_len

                

        
        """
        [AAABABB]
        []
        [A]
        [AA]
        [AAA]
        [AAAB]
        [AAABA]
        [AAABAB] -> Not valid! -> store this length -> start shrinking
        [AABAB] -> Not Valid! -> continue shrinking
        [ABAB] -> Not Valid! -> continue
        [BAB] -> Valid! new most_freq - B!
        [BABB] -> valid!
        r has ended, so there is not anything else to check
        """

        
        
        
        
        