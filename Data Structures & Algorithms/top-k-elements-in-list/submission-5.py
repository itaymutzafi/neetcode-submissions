from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # learn bucket sort!
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for num in counter:
            freq[counter[num]].append(num)
            
        res = []
        i = len(freq) - 1
        while len(res) < k and i >= 0:
            if freq[i]:
                for num in freq[i]:
                    if len(res) < k:
                        res.append(num)
                    else:
                        break
            i -=1
        return res
            
            
    
        