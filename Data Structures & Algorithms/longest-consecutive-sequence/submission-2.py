class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0
        for i in nums:
            if i -1 not in s:
                idx = 0
                while i + idx in s:
                    idx +=1
                longest = max(longest, idx)
        return longest

        