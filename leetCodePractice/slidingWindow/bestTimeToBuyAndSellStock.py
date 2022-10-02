class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxOutput = 0
        minPrice = prices[0]

        for price in prices:
            profit = price - minPrice
            maxOutput = max(maxOutput, profit)
            minPrice = min(minPrice, price)

        return maxOutput