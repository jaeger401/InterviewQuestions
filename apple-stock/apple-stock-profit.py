#!/usr/bin/env python
#
#   FILE: apple-stock-profit.py
# AUTHOR: jaeger401
#   DATE: Sun Nov  8 21:08:51 EST 2015
#  DESCR:
#

def get_max_profit(prices):
    buy = 0
    sell = 0
    prospective_buy = 0
    for x in prices:
        if buy == 0: buy = x 
        if prospective_buy == 0 or x < prospective_buy: 
            prospective_buy = x
        if x > sell: sell = x
        if (x - prospective_buy) > (sell - buy):
            sell = x
            buy = prospective_buy
    return (sell - buy) if (sell - buy) > 0 else 0

if __name__ == "__main__":
    #stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    #stock_prices_yesterday = [3, 5, 2, 3, 1, 4, 5]
    #stock_prices_yesterday = [5, 4, 3, 2, 1]
    #stock_prices_yesterday = [1, 2, 3, 4, 5]
    #stock_prices_yesterday = [1]
    stock_prices_yesterday = [2, 5, 1, 4, 3]
    print get_max_profit(stock_prices_yesterday)

