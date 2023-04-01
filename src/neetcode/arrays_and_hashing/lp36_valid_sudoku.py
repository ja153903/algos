class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row = f"row {i} => {board[i][j]}"
                    col = f"col {j} => {board[i][j]}"
                    box = f"box {i // 3} {j // 3} => {board[i][j]}"

                    hashes = [row, col, box]

                    if any([hash in seen for hash in hashes]):
                        return False

                    for hash in hashes:
                        seen.add(hash)

        return True
