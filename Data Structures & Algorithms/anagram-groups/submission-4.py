class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            curr = [0 for _ in range(26)]
            for ch in s:
                curr[ord(ch) - ord("a")] += 1
            curr = tuple(curr)
            if curr in d:
                d[curr].append(s)
            else:
                d[curr] = [s]
        
        return list(d.values())