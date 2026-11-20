class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we don't need to accoutn for the columns in the center of
        # the two columns
        # two pointers, left and right
        # converge the pointers, calculate the max area
        # max area can be derived from subtracting
        # right by the left pointer and multiplying it by
        # the heights of the smaller column
        # to calculate the greatest area
        # we only shift the pointer of the smaller column
        # every iteration

        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            distance = right - left
            area = min(heights[right], heights[left]) * distance
            result = max(area, result)

            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

        return result