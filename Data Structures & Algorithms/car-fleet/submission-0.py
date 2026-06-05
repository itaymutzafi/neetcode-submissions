class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highway = [(position[i], speed[i]) for i in range(len(speed))]
        highway.sort(key = lambda x: (x[0], x[1]), reverse = True)
        
        q = []
        for car in highway:
            t = (target - car[0]) / car[1]
            if not q or t > q[-1]:
                q.append(t) # the stack invariant - each t inserted is a fleet
        
        return len(q)
        
        
        
        
        


        
        

        
        
        
        