class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        counts = defaultdict(int)
        left = 0
        right = 0
        current = 0
        result = 0
        max_freq = 0

        while right < len(s):
            counts[s[right]] += 1
            current += 1
            max_freq = max(max_freq, counts[s[right]])

            # keep shrinking until valid again
            while current - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                current -= 1
        
            # window is valid this iteration
            # save result and move right
            result = max(result, current)
            right += 1
    
        return result