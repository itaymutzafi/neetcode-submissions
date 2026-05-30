class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices: [1,3,4,0,4]
        # in each i, you need to choose: you buy, you sell or you hold
        # you buy: you cannot sell the coin at the other day.
        # you sell: you get price - buy
        # you hold: you dont do nothing.
        memo = {}
        
        def rec(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            if buying:
                buy = rec(i + 1, False) - prices[i]
                hold = rec(i + 1, True)
                memo[(i, buying)] = max(buy, hold)
                return memo[(i, buying)]
            else:
                sell = prices[i] + rec(i+2, True)
                hold = rec(i+1, False)
                memo[(i, buying)] = max(sell, hold)
                return memo[(i, buying)]
        
        return rec(0, True)


        
            