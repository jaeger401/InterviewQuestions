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

###My Solution (in about 30-45 minutes)

This solution was not time-bounded the same as the other cases, since it 
was the first one I did and I hadn't set the ground rules yet. I completed 
the initial pass on this one while riding the train to an interview.

To be documented :)

