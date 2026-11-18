class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            distance = right - left
            height = min(heights[left], heights[right])

            result = max(height*distance, result)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return result
        # NVM, IGNORE THE COLUMNS IN THE CENTER, THIS Q IS NOT ASKING THAT
        # LOWER COLUMN * DISTANCE BETWEEN THE WALLS
        # SHIFT THE LOWER COLUMN OF THE TWO
        # RETURN THE GREATEST RESULT