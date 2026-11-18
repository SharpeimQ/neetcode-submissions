class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        start = 0
        end = len(string) - 1


        while start < end:
            # filter invalid start
            while not string[start].isalnum() and start < end:
                start += 1

            # filter invalid end
            while not string[end].isalnum() and start < end:
                end -= 1
            
            # check breaking cause
            if string[start] != string[end]:
                return False
            
            # ending inc/dec
            start += 1
            end -= 1

        return True