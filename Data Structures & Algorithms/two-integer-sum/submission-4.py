class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dictNums:
                dictNums[nums[i]] = i
            else:
                return [dictNums[diff], i]

