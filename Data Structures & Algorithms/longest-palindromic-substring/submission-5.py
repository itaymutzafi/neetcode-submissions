class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ""
        global_l, global_r = 0,0
        
        def check_pal(mid1, mid2):
            max_l, max_r = 0,0
            l, r = mid1, mid2

            while l >= 0 and r < len(s):
                if s[l] == s[r] and r - l >= max_r - max_l:
                    max_l, max_r = l, r
                    l -=1
                    r +=1
                else: 
                    break
            return max_l, max_r
        
        for i in range(len(s)):
            one_c_l, one_c_r = check_pal(i,i)
            if global_r - global_l <= one_c_r - one_c_l:
                global_l, global_r = one_c_l, one_c_r

            if i > 0 and s[i] == s[i-1]:
                two_c_l, two_c_r = check_pal(i-1, i)
                if global_r - global_l <= two_c_r - two_c_l:
                    global_l, global_r = two_c_l, two_c_r
        
        return s[global_l:global_r + 1]

                    