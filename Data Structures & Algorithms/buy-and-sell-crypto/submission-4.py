class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for n in prices:
            maxP = max(maxP, n - minBuy)
            minBuy = min(minBuy, n)
        return maxP