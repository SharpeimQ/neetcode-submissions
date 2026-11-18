class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for key, val in count.items():
            bucket[val].append(key)

        result = []

        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if k == len(result):
                    return result
