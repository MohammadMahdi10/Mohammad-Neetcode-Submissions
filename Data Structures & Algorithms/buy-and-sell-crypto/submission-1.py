class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for L in range(len(prices)):
            R = L + 1
            if R < len(prices):
                calculate = prices[R] - prices[L]

                while calculate > 0 and R < len(prices):
                    calculate = prices[R] - prices[L]
                    profit = max(profit, calculate)
                    R += 1
        
        return profit