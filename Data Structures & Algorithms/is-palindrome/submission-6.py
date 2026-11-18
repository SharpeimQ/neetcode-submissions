class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer solutoin
        left = 0
        right = len(s) - 1
        lower = s.lower()

        while left < right:
            while not lower[left].isalnum() and left < right:
                left += 1
            
            while not lower[right].isalnum() and left < right:
                right -= 1

            if lower[left] != lower[right]:
                return False
            
            left += 1
            right -= 1

        return True