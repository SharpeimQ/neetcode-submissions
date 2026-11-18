class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most frequent elements
        # frequency tracking hashmap [number => frequency]
        # Initialize 2D list of size input nums + 1 to account for 0-index
        # convert the hashmap into a sorted tuple or bucket arrays
        # iterate in reverse until you have the k most frequent
        from collections import defaultdict

        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1

        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])

        for num, frequency in hash.items():
            buckets[frequency].append(num)

        result = []

        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                result.append(num)

                if len(result) == k:
                    return result