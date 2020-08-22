from backend.YahooAPI import *
import pandas as pd
from settings import DATA_ROOT




ISIN_Shorts = pd.read_pickle(DATA_ROOT + "/FCAData/" + str("GB0007958233") + "_HFCA.pkl")
print(ISIN_Shorts)


ISIN_Shorts.set_index(ISIN_Shorts['Position Date'], inplace=True)
print(ISIN_Shorts)

