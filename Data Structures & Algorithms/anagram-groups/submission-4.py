class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        group_list = defaultdict(list)

        for word in strs:
            freq = defaultdict(int)
            for char in word:
                freq[char] += 1
            
            key = tuple(sorted(freq.items()))
            group_list[key].append(word)

        return list(group_list.values())