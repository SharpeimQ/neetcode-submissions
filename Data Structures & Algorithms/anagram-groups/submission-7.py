class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group hash outside that stores anagram signatures

        from collections import defaultdict

        groups = defaultdict(list)

        for string in strs:
            count = defaultdict(int)

            for char in string:
                count[char] += 1
            
            # convert the count hash into a hashable tuple
            signature = tuple(sorted(count.items()))
            groups[signature].append(string)
        
        return list(groups.values())