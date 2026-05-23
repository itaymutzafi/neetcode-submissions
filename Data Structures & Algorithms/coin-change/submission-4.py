class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.d = {}
        self.cnt = 0

        # 3
        # helper(1)
        # helper(-1)

        def helper(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if amount in self.d:
                return self.d[amount]

            min_coins = -1
            for i in range(len(coins)):
                tmp = helper(amount - coins[i])
                if tmp != -1:
                    if min_coins == -1 and tmp != -1:
                        min_coins = tmp + 1
                    else:
                        min_coins = min(min_coins, tmp + 1)
            
            self.d[amount] = min_coins
            return min_coins
        
        return helper(amount)
        
        
        