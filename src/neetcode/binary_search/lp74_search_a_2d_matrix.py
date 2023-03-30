class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_left, row_right = 0, len(matrix) - 1

        while row_left <= row_right:
            row_mid = row_left + (row_right - row_left) // 2

            row = matrix[row_mid]
            row_start, row_end = row[0], row[-1]

            if row_start <= target <= row_end:
                col_left, col_right = 0, len(matrix[0]) - 1

                while col_left <= col_right:
                    col_mid = col_left + (col_right - col_left) // 2

                    if matrix[row_mid][col_mid] == target:
                        return True
                    elif matrix[row_mid][col_mid] < target:
                        col_left = col_mid + 1
                    else:
                        col_right = col_mid - 1

                return False
            elif row_end < target:
                row_left = row_mid + 1
            else:
                row_right = row_mid - 1

        return False
