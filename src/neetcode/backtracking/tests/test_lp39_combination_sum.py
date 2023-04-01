from ..lp39_combination_sum import Solution

solution = Solution()


def test_combination_sum():
    assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
