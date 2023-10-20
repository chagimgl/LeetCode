from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_sum = 0
        local_max_profit = 0
        min_purchase = prices[0]
        increasing_order = True
        for i in range(1, len(prices)):
            if (prices[i] <= prices[i-1]):
                min_purchase = prices[i]
                profit_sum += local_max_profit
                local_max_profit = 0
                increasing_order = False
                continue
            
            current_profit = prices[i] - min_purchase
            if current_profit > local_max_profit:
                local_max_profit = current_profit
            if (i == len(prices) - 1):
                profit_sum += current_profit
        
        if increasing_order:
            return local_max_profit
        else:
            return profit_sum
        
        
        
solution = Solution()

prices = [6,1,3,2,4,7]
solution.maxProfit(prices)
