class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palidinrome is when a string is the same left to right
        # if you reverse it, it's the same string
        # why not just use reverse?
        # this questions asks about case-sensitivity and non alphanumeric characters

        # let's create a left and right pointer to track characters inside the input string
        # if the character at the left pointer is not alphanumeric, skip
        # if the character at the right pointer is not alphanumeric, skip
        # if the characters at the left and right pointers match, shrink the window
        # if the characters at the left and right pointers do not match, return False

        left = 0
        right = len(s) - 1
        lower = s.lower()
        while left < right:
            if not lower[left].isalnum():
                left += 1
                continue
            
            if not lower[right].isalnum():
                right -= 1
                continue

            if lower[left] == lower[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True