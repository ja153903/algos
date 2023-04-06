from ..lp853_car_fleet import Solution

solution = Solution()


def test_case():
    assert solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert solution.carFleet(10, [6, 8], [3, 2]) == 2
    assert solution.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    assert solution.carFleet(100, [0, 4, 2], [2, 1, 3]) == 1
