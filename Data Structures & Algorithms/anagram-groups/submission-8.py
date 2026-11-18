class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        group = defaultdict(list)
        for string in strs:
            count = defaultdict(int)
            for char in string:
                count[char] += 1

            sign = tuple(sorted(count.items()))
            group[sign].append(string)

        return list(group.values())
            


            