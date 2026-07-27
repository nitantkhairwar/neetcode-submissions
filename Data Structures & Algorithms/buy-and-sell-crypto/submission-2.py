class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute force
        min_value = float("inf")
        profit = 0
        for i in range(1, len(prices)):
            min_value = min(min_value, prices[i-1])
            print(min_value)
            profit = max(profit, prices[i] - min_value)
        return profit