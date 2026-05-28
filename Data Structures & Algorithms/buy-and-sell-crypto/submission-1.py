class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        if not prices:
            return max_prof
        
        lowest = prices[0]
        for i in range(1, len(prices)):
            max_prof = max(max_prof, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        
        return max_prof
