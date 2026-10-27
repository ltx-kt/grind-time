class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, o, prevH):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in o or heights[r][c] < prevH:
                return
            o.add((r, c))

            dfs(r - 1, c, o, heights[r][c])
            dfs(r + 1, c, o, heights[r][c])
            dfs(r, c - 1, o, heights[r][c])
            dfs(r, c + 1, o, heights[r][c])
        
        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols - 1, atl, heights[i][cols - 1])

        
        for i in range(cols):
            dfs(0, i, pac, heights[0][i])
            dfs(rows - 1, i, atl, heights[rows - 1][i])

        res = []
        print(pac)
        print(atl)
        for i in range(rows):
            for j in  range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res

