class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        current = 0

        # if the sell price is lower than the buy price
        #   it's not a winning trade, shift the left pointer to the right pointer (good buy)
        # else if the sell price is higher than the buy price
        #   it is a good trade, record the current and compare it to the best price

        # we don't have to measure all the trades by doing this optimization
        # O(n) TC

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                current = prices[right] - prices[left]
                result = max(current, result)
            
            right += 1
        
        return result