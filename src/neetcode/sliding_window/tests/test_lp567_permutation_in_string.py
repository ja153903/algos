from ..lp567_permutation_in_string import Solution

solution = Solution()


def test_cases():
    assert solution.checkInclusion("ab", "eidbaooo") is True
    assert solution.checkInclusion("ab", "eidboaoo") is False
    assert solution.checkInclusion("adc", "dcda") is True
