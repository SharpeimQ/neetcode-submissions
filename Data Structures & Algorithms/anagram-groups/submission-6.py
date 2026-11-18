class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # python hashes and arrays are not hashable
        # python outer hash to store anagram signatures and their strings
        # tuple signatures => array of matching strings
        # python inner hash to identify anagram signatures

        from collections import defaultdict

        outer = defaultdict(list)

        for string in strs:
            hash = defaultdict(int)
            for char in string:
                hash[char] += 1

            # tuple the hash signatures
            signature = tuple(sorted(hash.items()))
            # store the signature and append the string to right key
            outer[signature].append(string)
        
        return list(outer.values())
