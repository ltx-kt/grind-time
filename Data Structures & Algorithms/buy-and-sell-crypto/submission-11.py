class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProf = 0
        for i in prices:
            minBuy = min(minBuy, i)
            maxProf = max(maxProf, i - minBuy)
        
        return maxProf