class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the longest consecutive sequence does not have to be in order, so we can remove all
        # duplicates by forcing it into a set

        unique = set(nums)

        # what's great about sets is that you can lookup it's elements in constant TC, we can 
        # leverage this by checking if the next element(s) are available in the list to determine
        # the longest sequence

        # if number - 1 is detected, it is not the start of the sequence and we can skip this iteration
        # if number + 1 is detected, it is a start (after above check) and we can begin counting until
        # number + 1 doesn't exist inside the set

        longest = 0
        for num in nums:
            current = 1
            if num - 1 in unique:
                continue

            while num + 1 in unique:
                current += 1
                num += 1
            
            longest = max(current, longest)
            
        return longest
