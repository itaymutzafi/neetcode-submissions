class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [(30, 0)]
        # [(38,1)] -> [1]
        # [(38,1),(30,2)] -> [1,?,1,?]
        # [(38,1),(36,3),(35,4)]
        # [(40,5)] -> [1,4,1,2,1,?,?]
        # [(40,5),(28,6)] 
        # [1,4,1,2,1,0,0]

        res = [0 for _ in range(len(temperatures))]
        if not temperatures: 
            return []
        q = []
        
        for i in range(len(temperatures)):
            
            while q and q[-1][0] < temperatures[i]:
                _, j = q.pop()
                res[j] = i - j
            
            q.append((temperatures[i], i))
                
        return res
            

        
        