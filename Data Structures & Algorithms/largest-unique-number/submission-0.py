class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen_once = set()
        for n in nums:
            if n in seen_once:
                seen_once.remove(n)
            else:
                seen_once.add(n)
                
        if len(seen_once) == 0:
            return -1
        return max(seen_once)