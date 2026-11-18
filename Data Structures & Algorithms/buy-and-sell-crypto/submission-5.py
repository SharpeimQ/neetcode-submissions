class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        result = 0

        while right <= len(prices) - 1:
            # if the sell price is greater than the buy price
            # record the profit and compare
            # else
            # the current buy price is too high anyways, restart the window
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                result = max(profit, result)
            else:
                left = right
                
            right += 1

        return result