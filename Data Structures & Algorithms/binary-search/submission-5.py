class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        while l < r:
            mid = (r + l) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return mid
        return (r + l) // 2 if nums[(r + l) // 2] == target else -1