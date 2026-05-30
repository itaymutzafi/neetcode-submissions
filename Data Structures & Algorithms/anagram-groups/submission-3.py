class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (1, 0, 1, 0,....,0,1,..) : ["act",]
        
        d = {}

        for s in strs:
            tmp = [0 for _ in range(26)]
            for ch in s:
                tmp[ord(ch) - ord("a")] +=1
            
            tup_tmp = tuple(tmp)
            if tup_tmp in d:
                d[tup_tmp].append(s)
            else:
                d[tup_tmp] = [s]
        
        return list(d.values())
            