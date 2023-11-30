# Coding Ninja problem link--> https://www.codingninjas.com/studio/problems/best-time-to-buy-and-sell-stock_6194560?leftPanelTabValue=PROBLEM

def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    n=len(prices)
    minPrice=prices[0]
    maxProfit = 0
    for i in range(0,n):
        if prices[i]<minPrice:
            minPrice=prices[i]
        maxProfit = max(prices[i]-minPrice, maxProfit)
    return maxProfit
    pass
