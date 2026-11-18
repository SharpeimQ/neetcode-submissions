class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        result = 0
        while left < right:
            # shift the smaller column inward to collect max height
            # if they're the same height shift whatever
            # area is found by multpliying the distance between the columns and the min col
            # height
            distance = right - left
            if heights[left] < heights[right]:
                result = max(distance * heights[left], result)
                left += 1
            else:
                result = max(distance * heights[right], result)
                right -= 1        

        return result