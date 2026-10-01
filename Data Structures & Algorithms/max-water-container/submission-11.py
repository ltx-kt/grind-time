class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0
        while l < r:
            b = r - l
            h = min(heights[l], heights[r])
            a = b * h

            res = max(res, a)

            if heights[l] == h:
                l += 1
            else:
                r -= 1
        return res