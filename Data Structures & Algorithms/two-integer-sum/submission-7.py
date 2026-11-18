class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # trick is to find complementary pair using subtraction
        # store results in key-value [elem, index] pair and return indexes when there is a match

        traversed = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in traversed:
                return [traversed[pair], i]
            else:
                traversed[num] = i;