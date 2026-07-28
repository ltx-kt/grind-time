class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b = prices[0]

        for i in prices:
            b = min(b, i)
            p = max(p, i - b)
        
        return p