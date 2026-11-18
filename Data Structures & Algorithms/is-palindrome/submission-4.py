class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        string = s.lower()

        while start < end:
            while not string[start].isalnum() and start < end:
                start += 1
            
            while not string[end].isalnum() and start < end:
                end -= 1

            if string[start] != string[end]:
                return False

            start += 1
            end -= 1

        return True