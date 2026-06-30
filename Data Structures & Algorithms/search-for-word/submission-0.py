class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def search(r: int, c: int, index: int):
            if index == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols 
            or word[index] != board[r][c] or board[r][c] == '#'):
                return False
            board[r][c] = '#'
            res = (search(r + 1, c, index + 1) or
                search(r, c + 1, index + 1) or
                search(r - 1, c, index + 1) or
                search(r , c - 1, index + 1))
            board[r][c] = word[index]
            return res



        for i in range(rows):
            for j in range(cols):
                if search(i, j, 0):
                    return True
        return False
