import datetime as dt
from turtledemo.penrose import start

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb  # optional to set plot theme
import yfinance as yf

sb.set_theme()  # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        data = yf.download(self.symbol, start=self.start, end=self.end)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0] for col in data.columns]
        data.index = pd.DatetimeIndex(data.index)
        self.calc_returns(data)
        return data


    def calc_returns(self, data):
        data["Change"] = data["Close"].diff()
        data["Intant Return"] = np.log(data["Close"]).diff().round(4)

    def plot_return_dist(self):
        plt.hist(self.data["Instant Return"] * 100, bins=30, color="green", edgecolor="white")
        plt.xlabel("Instantaneous Return (%)")
        plt.ylabel("Number of Days")
        plt.title(f"Daily Instant Returns on Stock {self.symbol.upper()}")
        plt.show()

    def plot_performance(self):
        self.data["Cumulative Return"] = (self.data["Close"] / self.data["Close"].iloc[0]) - 1
        plt.plot(self.data.index, self.data["Cumulative Return"]*100, color="green")
        plt.axhline(y=0, color="grray", linestyle="--")
        plt.xlabel("Data")
        plt.ylabel("Cumulative Return (%)")
        plt.title(f"Performance of Stock {self.symbol} from {self.start} to {self.end}")
        plt.show()



def main():
    # uncomment (remove pass) code below to test
    # test = Stock(symbol=[stock_symbol]) # optionally test custom data range
    # print(test.data)
    # test.plot_performance()
    # test.plot_return_dist()
    test = Stock(symbol=["AAPL"])
    print(test.data)
    test.plot_performance()
    test.plot_performance()




if __name__ == '__main__':
    main()