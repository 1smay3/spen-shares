from backend.YahooAPI import *
import pandas as pd


print(YahooStockPrice("GB0007958233","2019-08-20", "2020-08-31"))

SIN_Prices = pd.read_pickle("C:/Users/spenc/PycharmProjects/spen-shares/data/FCAData/GB00B1JQDM80_HFCA.pkl")##


print(SIN_Prices)