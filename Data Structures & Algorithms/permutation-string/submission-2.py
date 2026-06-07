class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)    

        chars1 = [0 for _ in range(26)]
        for ch in s1:
            chars1[ord(ch) - ord("a")] +=1
        
        chars2 = [0 for _ in range(26)]
        for i in range(k-1):
            chars2[ord(s2[i]) - ord("a")] +=1
        
        l, r = 0, k-1
        
        while r < len(s2):
            chars2[ord(s2[r]) - ord("a")] +=1
            if chars1 == chars2:
                return True
            chars2[ord(s2[l]) - ord("a")] -=1
            r +=1
            l +=1                   
            
        return False