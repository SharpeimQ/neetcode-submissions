class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # record the longest substring length without duplicate characters
        # use two pointers, left and right
        # use a deque the keep track of the current substring
        # the set is reset for every substring
        # slide the right pointer until a duplicate is detected
        # if a duplicate is detected, shift the left pointer until there is no more duplicate inside the string
        # each shift of the left pointer, pop from the deck
        window = set()
        left = 0
        right = 0
        result = 0
        current = 0

        while right < len(s):
            # while duplicate detected, shrink the left window repeatedly
            while s[right] in window:
                window.remove(s[left])
                left += 1
                current -= 1
            
            # window is valid, add new character to substring
            window.add(s[right])
            current += 1
            result = max(result, current)

            right += 1

        return result