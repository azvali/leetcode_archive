def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0
    profit = 0
    l = 0
    for r in range(len(prices)):
        if r < len(prices) - 1 and prices[r] < prices[l]:
            l = r    
        profit = max(profit, prices[r] - prices[l])
    return profit