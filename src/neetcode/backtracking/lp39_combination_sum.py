class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        candidates.sort()

        self._backtrack(candidates, target, result, [], 0, 0)

        return result

    def _backtrack(self, candidates, target, result, current, current_sum, start):
        if target == 0:
            result.append(list(current))
            return

        for i in range(start, len(candidates)):
            candidate = candidates[i]

            if target - candidate >= 0:
                current.append(candidate)
                self._backtrack(
                    candidates,
                    target - candidate,
                    result,
                    current,
                    current_sum + candidate,
                    i,
                )
                current.pop()
