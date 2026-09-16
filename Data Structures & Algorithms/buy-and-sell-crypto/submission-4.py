class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        mbuy = float("inf")
        for i in range(1, len(prices)):
            mbuy = min(mbuy, prices[i-1])
            max_profit = max(max_profit, prices[i]-mbuy)
        return max_profit