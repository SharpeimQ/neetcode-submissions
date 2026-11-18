class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # identify anagrams by counting the strings with a hash
        # compare the hashes to see if they are matching anagrams
        # can optimize by word length

        from collections import defaultdict

        # hashes initialized to 0 in python
        counts = defaultdict(int)
        countt = defaultdict(int)

        for string in s:
            counts[string] += 1

        for string in t:
            countt[string] += 1
        
        return counts == countt