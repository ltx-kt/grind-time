class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h = defaultdict(list)
        v = defaultdict(list)
        s = defaultdict(list)

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                val = board[i][j]
                if val == '.':
                    continue
                if val in h[i] or val in v[j] or val in s[(i//3, j//3)]:
                    return False
                
                h[i].append(val)
                v[j].append(val)
                s[(i//3, j//3)].append(val)

        return True