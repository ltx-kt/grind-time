class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        res = 0

        def dfs(r, c):
            st = [[r, c]]

            while st:
                r1, c1 = st.pop()
                if (r1 < 0 or c1 < 0 or r1 >= rows or c1 >= cols or grid[r1][c1] == '0'):
                    continue

                grid[r1][c1] = '0'
                for dr, dc in directions:
                    st.append([r1 + dr, c1 + dc])
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res