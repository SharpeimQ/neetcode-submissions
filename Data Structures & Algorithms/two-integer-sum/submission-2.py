class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in hash:
                return [hash[pair], i]
            else:
                hash[num] = i

        return False