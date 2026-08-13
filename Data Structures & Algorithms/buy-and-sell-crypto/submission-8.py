class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        prof = 0
        for i in prices:
            buy = min(buy, i)
            prof = max(prof, i - buy)
        return prof