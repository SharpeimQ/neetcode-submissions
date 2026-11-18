class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the most frequent elements
        # optimize sorting by using array bucket sorting O(N)
        # read from the array in reverse until you have k elements

        from collections import defaultdict
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        # Initialize Bucket Array Size
        bucket = []
        for _ in range(len(nums)+1):
            bucket.append([])

        for key, val in count.items():
            bucket[val].append(key)

        result = []
        # iterate in reverse
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                if k == len(result):
                    return result
                
                result.append(num)
        
        return result
