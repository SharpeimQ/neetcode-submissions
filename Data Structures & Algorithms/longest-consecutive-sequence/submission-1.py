class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store the input list as a set so we can do instant element lookups
        # iterate through the input list/array:

        # if the current number - 1 exists inside the set:
        # it is not the start of the sequence, so we skip this iteration

        # if the current element - 1 doesn't exist inside the set:
        # it is the start of the sequence, begin counting:
        # while element + 1 is inside the set,
        # increment the longest count and save the greatest consecutive sequence

        # return the longest consecutive sequence
        
        unique = set(nums)
        result = 0
        for num in nums:
            current = 1

            if num - 1 in unique:
                continue
            
            while num + 1 in unique:
                current += 1
                num += 1
            
            result = max(current, result)

        return result