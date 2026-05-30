class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [5,8,2,8], cost = [6,5,6,6] 
        # [-1, 3, -4, 2]
        # 0 not possible, total is -1. 1 is possible. 2 is not possible, tot is -1. 3 is possible, total is 2

        total = 0
        res_i = 0

        for i in range(2 * len(gas)):
            total += (gas[i % len(gas)] - cost[i % len(gas)])
            if total < 0:
                total = 0
                res_i = i + 1
        
        if res_i < len(gas):
            return res_i
        return -1
                

        
                
                
                