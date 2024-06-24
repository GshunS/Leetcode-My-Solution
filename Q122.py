# 122. Best Time to Buy and Sell Stock II
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = {len(prices) - 1: 0}
    for i in range(len(prices) - 2, -1, -1):
        temp_max_profit = max(0, max(0, prices[i + 1] - prices[i]) + max_profit[i + 1])
        max_profit[i] = temp_max_profit
    return max_profit[0]


prices = [1, 2, 3, 4, 5]
print(maxProfit(prices))
