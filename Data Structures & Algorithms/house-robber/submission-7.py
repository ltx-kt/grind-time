class Solution:
    def rob(self, nums: List[int]) -> int:
        n_minus_2 = 0
        n_minus_1 = 0
        for n in nums:
            temp = max(n + n_minus_2, n_minus_1)
            n_minus_2 = n_minus_1
            n_minus_1 = temp
        return n_minus_1