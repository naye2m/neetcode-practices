class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profits = [0]
        for x in prices[1:]:
            profits.append(x - min_buy)
            print(max(profits),profits)
            if min_buy > x:
                min_buy = x
        return max(profits)