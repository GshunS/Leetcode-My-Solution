# 123. Best Time to Buy and Sell Stock III

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = []
    min_price = prices[0]
    for price in prices:
        min_price = min(min_price, price)
        profit.append(max(0, price - min_price))

    print(profit)
    max_price = prices[-1]
    total = 0
    max_profit = 0
    for i in range(len(prices) - 1, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, max_price - prices[i])
        total = max(total, profit[i] + max_profit)

    return total


prices = [3,3,5,0,0,3,1,4]
print(maxProfit(prices))
