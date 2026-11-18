class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # slight opt length guard
        if len(s) != len(t):
            return False
        
        from collections import defaultdict

        # hashes initialized to 0
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)

        # counting algo
        for char in s:
            s_hash[char] += 1

        for char in t:
            t_hash[char] += 1
        
        return s_hash == t_hash