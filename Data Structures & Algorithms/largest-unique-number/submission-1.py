class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hm = {}
        largest = -1
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        
        for k, v in hm.items():
            if v == 1:
                largest = max(k, largest)
        return largest