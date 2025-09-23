# Input: prices = [7,1,5,3,6,4]
# Output: 5


def best_time_to_buy_and_sell_stock(prices):
    lc = 0
    rc = 1
    max_profit = 0

    while(rc < len(prices)): 
        if(prices[lc] < prices[rc]):
            profit = prices[rc] - prices[lc]
            if(profit > max_profit):
                max_profit = profit
        else:
            lc = rc
        rc += 1
    return max_profit




print(best_time_to_buy_and_sell_stock([7,1,5,3,6,4]))