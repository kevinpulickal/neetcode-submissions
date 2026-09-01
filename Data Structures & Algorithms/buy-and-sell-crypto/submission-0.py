class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):

            if prices[right] > prices[left]:
                current = prices[right] - prices[left]

                if current > profit:
                    profit = current

            elif prices[right] < prices[left]:
                left = right

            right += 1
            
        return profit
