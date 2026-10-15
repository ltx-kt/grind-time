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
                maxL = max(maxL, height[l])
                res += max(maxL - height[l], 0)
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += max(maxR - height[r], 0)
        return res
