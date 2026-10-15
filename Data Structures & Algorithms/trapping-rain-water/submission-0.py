class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        maxL = height[l]
        maxR = height[r]
        while l < r:

            if maxL < maxR:
                l += 1
                res += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])
            else:
                r -= 1
                res += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])
        return res
