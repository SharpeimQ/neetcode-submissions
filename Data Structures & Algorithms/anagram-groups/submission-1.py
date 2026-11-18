class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        list_dict = defaultdict(list)

        for word in strs:
            count = defaultdict(int)
            for char in word:
                count[char] += 1
            
            key = tuple(sorted(count.items()))
            list_dict[key].append(word)

        return list(list_dict.values())