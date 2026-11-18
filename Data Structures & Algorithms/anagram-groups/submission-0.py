class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)
        for word in strs:
            hash = defaultdict(int)

            for char in word:
                hash[char] += 1

            key = tuple(sorted(hash.items()))
            groups[key].append(word)
        
        return list(groups.values())