# 121. Best Time to Buy and Sell Stock
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = {len(prices) - 1: 0}
    max_num = prices[-1]
    for i in range(len(prices) - 2, -1, -1):
        max_profit[i] = max(max_num - prices[i], max_profit[i + 1])
        max_num = max(max_num, prices[i])
    return max_profit[0]


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
