class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count all numbers by frequency using a hash
        
        # convert the hash into bucket arrays with freq indexes
        # initialize a 2d list of nums + 1 length to store all possible freq

        # hash (number, freq) => array [freq index] => nums at index
        # read from the array until you have k elements

        from collections import defaultdict

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])

        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
