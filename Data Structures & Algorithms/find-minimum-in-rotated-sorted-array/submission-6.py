class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                res = min(res,nums[l])
                l = m + 1
            else:
                r = m - 1
        return res