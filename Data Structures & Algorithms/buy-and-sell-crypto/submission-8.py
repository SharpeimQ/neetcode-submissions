class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force solution
        # calculate all the combinations in O(n^2)
        # we don't have to calculate all the combinations
        # we only should record when the sell price > buy price
        # two pointers, left and right
        # left = buy day, 0
        # right = sell day, left + 1

        # if the sell price < buy price or
        # if prices[right] < prices[left]
        #   skip calculation
        #   move the buy day to that sell day
        # else if it's profitable
        #   record the current profit
        #   save the greatest profit
        #   move the right pointer to see if there's a better deal

        # return the result

        left = 0
        right = left + 1
        current = 0
        result = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                current = prices[right] - prices[left]
                result = max(current, result)
                right += 1
        
        return result

