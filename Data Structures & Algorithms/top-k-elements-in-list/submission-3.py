class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # let's count the frequency with a hash, standard algo
        from collections import defaultdict
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        # 2D list/array to hold all possible frequencies
        # [1, 2, 3, 4, 5, 6]
        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])

        # num => freq
        # list[freq].append(num)
        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
