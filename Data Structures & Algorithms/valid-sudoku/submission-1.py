class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrid = [[set() for _ in range(3)] for _ in range(3)] 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in cols[c]:
                    print("failed in cols")
                    return False

                if board[r][c] in rows[r]:
                    print("failed in rows")
                    return False

                if board[r][c] in subgrid[r // 3][c // 3]:
                    print(f"c:{c}\t\t subgrid[[{r // 3}]{3 // 3}]: {subgrid[r // 3][c // 3]}")
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                subgrid[r // 3][c // 3].add(board[r][c])

                

        return True
