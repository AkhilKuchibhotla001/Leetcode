class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -prices[0]
        sell = 0
        cool = 0

        for i in range(1 , len(prices)):
            new_buy = max(buy , cool - prices[i])

            new_sell = buy + prices[i]

            new_cool = max(cool , sell)

            buy = new_buy

            sell = new_sell

            cool = new_cool
        return max(sell , cool)
        