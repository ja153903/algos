from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            # sort the string to group anagrams
            groups["".join(sorted(s))].append(s)

        return list(groups.values())
