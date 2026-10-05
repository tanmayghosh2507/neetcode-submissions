class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            nums = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                elif int(board[i][j]) < 1 or int(board[i][j]) > 9 or board[i][j] in nums:
                    return False
                else:
                    nums.add(board[i][j])
        
        for i in range(m):
            nums = set()
            for j in range(n):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in nums:
                    return False
                else:
                    nums.add(board[j][i])
        
        row_starts = [0, 3, 6]
        col_starts = [0, 3, 6]
        row = True

        for i in range(len(row_starts)):
            for j in range(len(col_starts)):
                row_start = row_starts[i]
                col_start = col_starts[j]
                nums = set()
                for row in range(row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] in nums:
                            return False
                        else:
                            nums.add(board[row][col])
        
        return True