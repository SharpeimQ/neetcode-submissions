class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        result = 0

        while right <= len(prices) - 1:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                result = max(profit, result)
            else:
                left = right
            
            right += 1
        
        return result