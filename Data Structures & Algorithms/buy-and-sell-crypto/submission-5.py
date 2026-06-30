class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)):
        #     endIdx = i + 1
        #     while endIdx < len(prices):
        #         max_profit = max(max_profit, prices[endIdx] - prices[i])
        #         endIdx += 1

        # return max_profit

        # l,r = 0, 1
        # maxm = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         maxm = max(maxm, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return maxm

        min_price = prices[0]
        max_profit = 0

        for sell in prices:
            max_profit = max(max_profit, sell - min_price)
            min_price = min(min_price, sell)
        
        return max_profit

