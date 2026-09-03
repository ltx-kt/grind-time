class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        minBuy = prices[0]

        for i in prices:
            minBuy = min(minBuy, i)
            prof = max(prof, i - minBuy)
        return prof