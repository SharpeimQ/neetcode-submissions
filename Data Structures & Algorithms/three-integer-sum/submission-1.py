class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        length = len(sort) - 1
        result = []

        for i, _ in enumerate(sort):
            left = i + 1
            right = length

            if sort[i] == sort[i - 1] and i > 0:
                continue
            
            while left < right:
                if sort[left] + sort[right] + sort[i] > 0:
                    right -= 1
                elif sort[left] + sort[right] + sort[i] < 0:
                    left += 1
                elif sort[left] + sort[right] + sort[i] == 0:
                    result.append([sort[left], sort[right], sort[i]])
                    left += 1
                    right -= 1
                    while sort[left] == sort[left - 1] and left < right:
                        left += 1
        
        return result