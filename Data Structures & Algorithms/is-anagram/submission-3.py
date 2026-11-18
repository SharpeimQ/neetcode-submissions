class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for char in s:
            hash_s[char] += 1
        
        for char in t:
            hash_t[char] += 1

        return hash_s == hash_t