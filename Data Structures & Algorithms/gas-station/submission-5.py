class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [5,8,2,8], cost = [6,5,6,6] 
        # [-1, 3, -4, 2]
        # 0 not possible, total is -1. 1 is possible. 2 is not possible, tot is -1. 3 is possible, total is 2

        total = 0
        tank = 0
        res_i = 0

        for i in range(len(gas)):
            curr = gas[i] - cost[i]
            total += curr
            tank += curr

            if tank < 0:
                tank = 0
                res_i = i + 1
        
        if total >= 0:
            return res_i
        else:
            return -1
        
        # before i it can not be that a gas station is valid (between i and the last start), since:
        # be a valid gas station start <= j <= i
        # so S(start, j) >= 0
        # and S(start, i) <= 0, since we met the condition
        # so S(j,i) = s(start, i) - s(start, j) <= 0
        # but if j is valid start, we can go from j to i. condridaction
                

        
                
                
                