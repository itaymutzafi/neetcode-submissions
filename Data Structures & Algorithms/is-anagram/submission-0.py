class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if s and t are not the same length, they can't be anagrams.
        if len(s) != len(t):
            return False

        # from this point, the assume is that s and t has the same length

        chars = [0 for _ in range(26)]
        
        for i in range(len(s)):
            chars[ord(s[i]) - ord("a")] += 1
            chars[ord(t[i]) - ord("a")] -= 1

        if any(chars) == 0:
            return True
        else:
            return False