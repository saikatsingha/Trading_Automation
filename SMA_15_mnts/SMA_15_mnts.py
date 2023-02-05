import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

yf.pdr_override() 
now = dt.datetime.now() 
stock = input("Enter the stock ticker: ")

startyear = 2022
startmonth = 1
startday = 1
start = dt.datetime(startyear, startmonth, startday) # set starting time for datasample
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock,start, now)
print(df)

df=df.iloc[ma:]

ma = 50
smaString = "SMA_" + str(ma)
ema = 30
emaString = "EMA_" + str(ma)

df[smaString] = df.iloc[:,4].rolling(window=ma).mean()

numH = 0
numC = 0

for i in df.index:
    if(df["Adj Close"][i]>df[smaString][i]):
        print("The close is higher than SMA.")
        numH = numH + 1
    else:
        print("The close is lower than SMA.")
        numC = numC + 1
print("The close is higher than SMA {} times.".format(str(numH)))
print("The close is lower than SMA {} times.".format(str(numC)))

x = df.index
y = df["Adj Close"]
z = df["SMA_50"]

title = (stock, "Adjusted Close price till date and 50 SMA")

def df_plot(data, x, y, title="", xlabel = "Date", ylabel = "Adj Close", dpi =100):
    plt.figure(figsize=(16,5), dpi = dpi)
    plt.plot(x,y, color = "tab:blue")
    plt.plot(z, color = "tab:red")
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

df_plot(df, x, y, title=title, xlabel = "Date", ylabel = "Value", dpi =100)