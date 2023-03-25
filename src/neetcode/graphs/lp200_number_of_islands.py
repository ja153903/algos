class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self._dfs(grid, row, col)
                    islands += 1

        return islands

    def _dfs(self, grid: list[list[str]], row: int, col: int) -> None:
        rows, cols = len(grid), len(grid[0])

        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1":
            return

        grid[row][col] = "#"

        self._dfs(grid, row + 1, col)
        self._dfs(grid, row - 1, col)
        self._dfs(grid, row, col + 1)
        self._dfs(grid, row, col - 1)
