from collections import defaultdict
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        right = 0
        current = 0
        result = 0
        max_freq = 0

        while right < len(s):
            # how can we check if a substring is valid?
            # formula:
            # current - max_freq > k INVALID
            # add the character at the right pointer
            # update the count
            # update the max freq
            count[s[right]] += 1
            current += 1
            max_freq = max(count[s[right]], max_freq)

            # while invalid, shrink
            while current - max_freq > k:
                count[s[left]] -= 1
                current -= 1
                left += 1
                max_freq = max(count.values())

            # after it's valid, save the max
            # add the right pointer only after everything
            result = max(current, result)
            right += 1


            
        return result