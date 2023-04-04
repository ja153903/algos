from ..lp153_find_minimum_in_rotated_sorted_array import Solution


solution = Solution()


def test_cases():
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([11, 13, 15, 17]) == 11
