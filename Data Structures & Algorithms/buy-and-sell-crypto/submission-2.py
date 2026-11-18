class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # have to buy first then sell
        # two pointers / sliding window
        # buy at left, subtract all values using other pointer traversal and save the max
        # increment left, reset right to left + 1 and do it over and over again

        left = 0
        while left < len(prices) - 1:
            right = left + 1
            while right < len(prices):
                profit = prices[right] - prices[left]
                result = max(profit, result)
                right += 1

            left += 1
            
        if result < 0:
            result = 0

        return result