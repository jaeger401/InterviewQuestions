##Apple Stock Price Profit Calculation

######Source: One of my five free questions on [interviewcake.com]()

###The Problem

Suppose we could access yesterday's stock prices as a list, where:

* The indices are the time in minutes past trade opening time, which was
  9:30am local time.
* The values are the price in dollars of Apple stock at that time.

So if the stock cost $500 at 10:30am, `stock_prices_yesterday[60] = 500`.

Write an efficient function that takes `stock_prices_yesterday` and returns
the best profit I could have made from 1 purchase and 1 sale of 1 Apple
stock yesterday.

For example:

```python
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
```

No "shorting"—you must buy before you sell. You may not buy and sell in the
same time step (at least 1 minute must pass).

###My Solution (in about 30-45 minutes total)

This solution was not time-bounded the same as the other cases, since it 
was the first one I did and I hadn't set the ground rules yet. I completed 
the initial pass on this one while riding the train to an interview. The 
writeup below is derived from the thought process I followed, backed up by 
the page of notes I took.

####Working Out The Logic

There are a series of interesting cases to solve here:

1. Steadily descending (no profit), e.g.: 5, 4, 3, 2, 1
2. Steadily ascending (all profit), e.g.: 1, 2, 3, 4, 5
3. Cases where the first profit is less than later profit, e.g.: 3, 4, 2, 1, 5
4. Cases where the first profit is greater than or equal to later profit, e.g.: 2, 5, 1, 4, 3

We could very easily solve this with a bubble-sort style scan through the prices, at the huge cost of O(n<sup>2</sup>). I suspect we can solve this in O(n) with a single pass by tracking the current best profit and switching to a new profit once we confirm it's possible to do better.

####The Algorithm

In order to track current profit, we'll need to hold on to the best **buy** and **sell** prices we've seen thus far.
To track the possibility of a better profit, we should need to track a **prospective buy** price only -- once we confirm that a given **sell** price would produce a better profit with the **prospective buy** price, then we'll use that pair of prices and start tracking a new **prospective buy** price.

Basically:

1. Scan forward until we find a profit of any sort. 
2. If we find a higher sell price, we'll swap that in for the one we have.
3. Continue to scan forward until we find a buy price that's lower than what we've already got.
4. Once we have a prospective buy price, check each sell price to see if it will produce a better profit.
  * If so, we have a new buy and sell price.

###My Code

I hand-simulated a couple cases using examples 1-4 above, and derived the following pseudo-code:

```
## Assumes variables for buy, sell, profit, prospective_buy, and prospective_profit
x = next_value_from_array
if x < buy && x < prospective_buy
  prospective_buy = x
if x > sell {
  sell = x
  profit = sell - buy
  prospective_profit = sell - prospective_buy
  if prospective_profit > profit {
    buy = prospective_buy
    profit = prospective_profit
  }
}
```

*Editor's note: this pseudo-code has numerous bugs, the greatest of which is that it doesn't catch better prospective profits that result from <b>lower</b> sell prices; e.g., 3, 5, 1, 4, 2. See [apple-stock-profit.py]() for a bug-fixed version. Fixing it took about 20-30 minutes of additional thought.*
