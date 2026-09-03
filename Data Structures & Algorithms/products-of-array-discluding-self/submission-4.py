class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = []
        for n in nums:
            res.append(pre)
            pre *= n
        
        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res