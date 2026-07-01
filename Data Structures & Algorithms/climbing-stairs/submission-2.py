class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1
        for i in range(n):
            res = x + y
            x = y
            y = res
        return y