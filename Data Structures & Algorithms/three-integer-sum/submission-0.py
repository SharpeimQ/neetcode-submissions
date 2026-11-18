class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        length = len(nums) - 1
        result = []

        for i, _ in enumerate(sort):
            # duplicate check
            if i > 0 and sort[i] == sort[i-1]:
                continue
            
            left = i + 1
            right = length 

            while left < right:
                # If sum is less, increase by incrementing left
                if sort[left] + sort[right] + sort[i] < 0:
                    left += 1
                # If sum is more, decrease by decrementing right
                elif sort[left] + sort[right] + sort[i] > 0:
                    right -= 1
                # THIS IS A RESULT
                elif sort[left] + sort[right] + sort[i] == 0:
                    result.append([sort[left], sort[right], sort[i]])    
                    left += 1
                    right -= 1
                    # duplicate check of previously traversed left solution
                    while sort[left] == sort[left - 1] and left < right:
                        left += 1
        
        return result
            # iterate through the nums list
            # sort the list first, so we can check all combinations
            # left to right negatives first
            # goal is to find triplets that sum to 0
            # in every iteration, we check:
            #  i, left, right
            #  if the sum of all three is greater than 0
            #    decrement right to decrease val
            #  if the sum of all three is less than 0
            #    increment left to increase the sum
            #  keep checking until it's valid: left < right
            # append the results to a result array gg

        