class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start, max_len = 0, 0
        for end in range(len(s)):
            if s[end] in seen:
                start = max(start, seen[s[end]] + 1)

            max_len = max(max_len, end - start + 1)
            seen[s[end]] = end

        return max_len
