class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edge = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in edge or board[r][c] == 'X':
                return
            edge.add((r, c))
            dfs (r + 1, c)
            dfs (r - 1, c)
            dfs (r, c + 1)
            dfs (r, c - 1)


        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols -1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows -1,  c)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in edge:
                    board[i][j] = "X"