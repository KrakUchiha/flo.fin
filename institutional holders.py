# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 01:36:18 2020

@author: afolabi
"""
import yfinance as yf
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
Def institutions_holding():
    Tickers = ('apvo')
    for x in Tickers:
    stock = yf.Ticker(Tickers)
    # show major holders
    A=stock.major_holders
    B=stock.institutional_holders
    print(A)
    print(B)
    # show institutional holders
institutions_holding()
    
