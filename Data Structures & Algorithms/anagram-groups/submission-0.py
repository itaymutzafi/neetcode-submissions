class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # approach - build dic which the key is the sorted anagram, and the val is a list
        # assume - each two anagrams sorted profile is the same.

        d = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in d:
                d[sorted_s].append(s)
            else:
                d[sorted_s] = [s]
        
        return list(d.values())
            