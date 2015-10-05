#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# Commenting out pre-entered code
"""
money = 1000.00
print(money)
"""

# Buying
# Lakshmi bought 2000 shares.
shares_bought = 2000

# When Lakshmi purchased the stock, she paid $900.00 per share.
purchase_amount = shares_bought * 900  # >>> 1800000

# Lakshmi paid her stockbroker a commission that = 3 percent of the amount she paid for the stock.
purchase_commission = purchase_amount * 0.03  # >>> 54000.0

# Selling
# Lakshmi sold 2000 shares.
shares_sold = 2000

# She sold the stock for $942.75 per share.
sell_amount = shares_sold * 942.75  # >>> 1885500.0

# She paid his stockbroker another commission that = 3 percent of the amount she received for the stock
sell_commission = sell_amount * 0.03  # >>> 56565.0


# Write a program to calculate and display the amount of money that
# Lakshmi had left when she sold the stock and paid her broker (both times)
money_paid = purchase_amount + purchase_commission  # >>> 1854000.0
money_made = sell_amount - sell_commission  # >>> 1828935.0

money_left = money_made - money_paid  # >>> -25065.0, Lakshmi did not make a profit.

print(money_left)
