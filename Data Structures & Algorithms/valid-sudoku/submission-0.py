class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        subsqr = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in subsqr[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                subsqr[(r//3,c//3)].add((board[r][c]))
        return True
                

        