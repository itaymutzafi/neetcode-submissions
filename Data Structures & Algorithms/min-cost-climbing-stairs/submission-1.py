class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if not cost:
            return 
            
        last = cost[1]
        last_last = cost[0]
        
        for i in range(2, len(cost) + 1):
            curr_cost = cost[i] if i < len(cost) else 0
            curr = min(curr_cost + last, curr_cost + last_last)
            last_last = last
            last = curr
            
        
        return curr