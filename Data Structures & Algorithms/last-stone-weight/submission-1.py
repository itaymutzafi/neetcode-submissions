class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stone = max(stones)
        bucket = [0] * (max_stone + 1)
        
        for stone in stones:
            bucket[stone] +=1
        
        first = second = max_stone
        
        while first > 0:
            if bucket[first] % 2 == 0:
                first -=1
            
            else: 
                j = min(second, first - 1)
                while j > 0 and bucket[j] == 0:
                    j -=1
                if j == 0:
                    return first # it means we don't have nothing else to check
                
                new_stone = first - j
                bucket[first] -=1
                bucket[j] -=1
                second = j
                bucket[new_stone] +=1
            
        return first
                    
        
                
                