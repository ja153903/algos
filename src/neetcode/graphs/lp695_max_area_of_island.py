class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    cur = self._dfs(grid, row, col)
                    ans = max(ans, cur)

        return ans

    def _dfs(self, grid: list[list[int]], row: int, col: int) -> int:
        if (
            row < 0
            or col < 0
            or row >= len(grid)
            or col >= len(grid[0])
            or grid[row][col] != 1
        ):
            return 0

        grid[row][col] = -1

        return (
            1
            + self._dfs(grid, row + 1, col)
            + self._dfs(grid, row - 1, col)
            + self._dfs(grid, row, col + 1)
            + self._dfs(grid, row, col - 1)
        )
