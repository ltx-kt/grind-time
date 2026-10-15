class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        hm = defaultdict(int)

        for n in nums:
            hm[n] = max(hm[n], hm[k]) + 1
            res = max(res, hm[n] - hm[k])
        return hm[k] + res