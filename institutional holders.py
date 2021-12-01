# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 01:36:18 2020

@author: afolabi
"""
import yfinance as yf
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

Tickers = ('apvo')



for x in Tickers:
    kxin = yf.Ticker(Tickers)

# show major holders
A=kxin.major_holders
B=kxin.institutional_holders


print(A)
print(B)

# show institutional holders
