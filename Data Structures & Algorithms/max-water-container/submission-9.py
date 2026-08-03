class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0
        while l < r:
            b = r - l
            h = min(heights[l], heights[r])
            a = b * h
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            res = max(res, a)
        return res
