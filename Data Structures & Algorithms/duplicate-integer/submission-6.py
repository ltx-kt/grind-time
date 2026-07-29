class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()
        for i in nums:
            if i in numberSet:
                return True
            numberSet.add(i)
        return False