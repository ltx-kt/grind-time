class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProf = 0
        for i in prices:
            maxProf = max(maxProf, i - minBuy)
            minBuy = min(minBuy, i)

        return maxProf