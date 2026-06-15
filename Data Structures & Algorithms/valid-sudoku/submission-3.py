class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = collections.defaultdict(set) # this creates a dictionary of sets

        # (tuple) : val

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    columns[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        
        return True