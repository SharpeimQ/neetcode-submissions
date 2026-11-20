class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring without repeating characters
        # left and right pointer, left marks left endpoint
        # right marks right substring endpoint
        # 
        # we can use a set to detect duplicate characters fast
        # traverse through the array of characters
        # while the character is a duplicate
        #   meaning the character at the right pointer is inside set
        #   we shrink the substring from the leftside until no dup
        #   left += 1
        #   set.remove(s[left])
        # else if there is no duplicates: valid
        #   right += 1
        #   set.add(s[right])
        #   save the longest length
        #
        # return the final result

        left = 0
        right = 0
        seen = set()
        current = 0
        result = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                current -= 1
            
            seen.add(s[right])
            right += 1
            current += 1
            result = max(current, result)

        return result

