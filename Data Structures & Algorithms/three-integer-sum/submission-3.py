class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # left and right pointers
        # window slides with index pointer, converging left and right
        result = []
        nums.sort()

        for i, _ in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            
            if nums[i] == nums[i-1] and i > 0:
                continue

            while left < right:
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] == 0:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result