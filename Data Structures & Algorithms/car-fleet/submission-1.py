class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highway = [(position[i], speed[i]) for i in range(len(speed))]
        highway.sort(key = lambda x: (x[0], x[1]), reverse = True)
        
        last_fleet = None
        fleets = 0
        for car in highway:
            t = (target - car[0]) / car[1]
            if not last_fleet or t > last_fleet:
                last_fleet = t 
                fleets +=1
        
        return fleets
        
        
        
        
        


        
        

        
        
        
        