class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        counts = defaultdict(int)
        left = 0
        right = 0
        current = 0
        result = 0
        max_freq = 0

        # we can solve this in one iteration
        while right < len(s):
            # update freq of the elem at right pointer
            # update the length of the current string
            # count the max freq, doesn't have to be accurate
            counts[s[right]] += 1
            current += 1
            max_freq = max(max_freq, counts[s[right]])

            # if current is an invalid string
            #   if the current string - max freq > k
            #   we cannot replace all the mismatched chars
            # keep shrinking until valid again
            while current - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                current -= 1
                max_freq = max(counts.values())
        
            # window is valid this iteration
            # save result and move right!
            result = max(result, current)
            right += 1
    
        return result