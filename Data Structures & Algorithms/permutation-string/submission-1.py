class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:           
        if not s1:
            return True
        if len(s1) > len(s2):
            return False

        chars_cnt = {}
        for ch in s1:
            chars_cnt[ch] = chars_cnt.get(ch, 0) + 1

        valid_chars = 0
        
        l, r = 0, len(s1) - 1
        for i in range(l, r + 1):
            curr = s2[i]
            if curr in chars_cnt:
                chars_cnt[curr] -=1
                if chars_cnt[curr] == 0:
                    valid_chars +=1
        
        if valid_chars == len(chars_cnt):
            return True

        if s2[l] in chars_cnt:
            if chars_cnt[s2[l]] == 0:
                valid_chars -=1
            chars_cnt[s2[l]] +=1
        l +=1
        r +=1
        
        while r < len(s2):
            new_ch = s2[r]
            if new_ch in chars_cnt:
                chars_cnt[new_ch] -=1
                if chars_cnt[new_ch] == 0:
                    valid_chars +=1
            if valid_chars == len(chars_cnt):
                return True
            
            if s2[l] in chars_cnt:
                if chars_cnt[s2[l]] == 0:
                    valid_chars -=1
                chars_cnt[s2[l]] +=1

            l +=1
            r +=1
        
        return False

                

