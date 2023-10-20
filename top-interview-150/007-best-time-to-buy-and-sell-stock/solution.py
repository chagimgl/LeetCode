from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]
        for i in range(1, len(prices)):
            current_profit = prices[i] - min_purchase
            if current_profit > max_profit:
                max_profit = current_profit
            if (prices[i] < min_purchase):
                min_purchase = prices[i]
        return max_profit        
        
solution = Solution()

prices = [7,6,4,3,1]
solution.maxProfit(prices)
