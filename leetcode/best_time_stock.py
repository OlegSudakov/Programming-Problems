# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_buy = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            prices[i] -= min_buy
        return max(prices + [0])
