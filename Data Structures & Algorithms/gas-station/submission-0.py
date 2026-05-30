class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            tank = 0
            valid = True
            for j in range(n):
                curr = (i+j) % n
                tank -= (cost[curr] - gas[curr])
                if tank < 0:
                    valid = False
                    break
                print(f" i is {i} and curr is: {curr} tank is {tank}")
            if valid:
                return i
        return -1
                
                
                