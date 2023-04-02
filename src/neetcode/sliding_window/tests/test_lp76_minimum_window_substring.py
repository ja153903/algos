from ..lp76_minimum_window_substring import Solution


solution = Solution()


def test_case():
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert solution.minWindow("a", "a") == "a"
    assert solution.minWindow("a", "aa") == ""
