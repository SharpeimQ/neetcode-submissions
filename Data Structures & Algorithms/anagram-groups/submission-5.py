class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group the like anagrams inside a dictionary
        # where anagram sig key with words as values
        # use count freq hash algo to identify like anagrams
        # python cant hash dictionaries so convert the count_freq into tuple

        from collections import defaultdict

        groups = defaultdict(list)

        for word in strs:
            count_dict = defaultdict(int)

            for char in word:
                count_dict[char] += 1

            key = tuple(sorted(count_dict.items()))
            groups[key].append(word)
        
        return list(groups.values())