class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        current = 0
        result = 0

        while right < len(s):
            # if the window is invalid, shrink the substring until it is valid
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                current -= 1

            # if the window is valid, we add to the substring
            seen.add(s[right])
            current += 1
            right += 1
            result = max(current, result)

        return result