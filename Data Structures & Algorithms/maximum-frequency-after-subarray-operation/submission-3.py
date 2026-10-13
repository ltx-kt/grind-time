class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        hm = {}

        res = 0

        for n in nums:
            hm[n] = max(hm.get(n, 0), hm.get(k, 0)) + 1
            res = max(res, hm[n] - hm.get(k, 0))

        return hm.get(k,0) + res