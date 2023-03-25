class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i])
            profit = max(profit, prices[i] - min_buy)

        return profit
