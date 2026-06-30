class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            endIdx = i + 1
            while endIdx < len(prices):
                max_profit = max(max_profit, prices[endIdx] - prices[i])
                endIdx += 1
            
        return max_profit

        