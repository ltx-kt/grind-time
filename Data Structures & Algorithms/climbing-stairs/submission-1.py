class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1
        for i in range(n):
            temp = x + y
            x = y
            y = temp
        return y
