class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i, x in enumerate(prices):
            if x < min_price: m
                in_price = x
                
            if x - min_price > max_profit:
                max_profit = x - min_price
        return max_profit
