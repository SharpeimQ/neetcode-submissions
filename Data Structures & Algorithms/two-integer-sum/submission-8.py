class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # find the complementary pair by subtracting the target with the current element at the index
        # hashes can be used to map an element to its index and allow us to store traversed elements

        hash = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in hash:
                return [hash[pair], i]
            
            hash[num] = i

        