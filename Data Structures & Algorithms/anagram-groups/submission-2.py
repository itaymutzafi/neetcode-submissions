from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # approach - build dic which the key is the sorted anagram, and the val is a list
        # assume - each two anagrams sorted profile is the same.

        d = defaultdict(list)
        for s in strs:
            chars = [0 for _ in range(26)]
            for ch in s:
                chars[ord(ch) - ord("a")] +=1
            d[tuple(chars)].append(s)
        
        return list(d.values())
            