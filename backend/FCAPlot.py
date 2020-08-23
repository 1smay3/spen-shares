import pandas as pd
import plotly.graph_objects as go
from settings import DATA_ROOT
import numpy as np
from backend.ChartPlotter import validrangefinder

# TEST WITH ISIN


def FCAPlot(ISIN):
    #Import Prices
    try:
        ISIN_Prices = pd.read_pickle(DATA_ROOT + "/YAHOOPRICES/" + str(ISIN) + "_HPRI.pkl")
    except FileNotFoundError:
        ISIN_Prices = pd.read_pickle(DATA_ROOT + "/YAHOOPRICES/" + "GB00B6XZKY75" + "_HPRI.pkl")

    try:
        ISIN_Shorts = pd.read_pickle(DATA_ROOT + "/FCAData/" + str(ISIN) + "_HFCA.pkl")
    except FileNotFoundError:
        ISIN_Shorts = pd.read_pickle(DATA_ROOT + "/FCAData/" + "GB00B6XZKY75" + "_HFCA.pkl")

    # This cant deal with duplicate indexes. Change it so that if there is a duplicate index, it combines the names to 'x and y'
    # For now, just drop dupes

    #Reindex to date
    ISIN_Shorts.set_index(ISIN_Shorts['Position Date'], inplace=True)
    ISIN_Shorts = ISIN_Shorts[~ISIN_Shorts.index.duplicated(keep='first')]

    tester = pd.concat([ISIN_Prices, ISIN_Shorts], axis=1)





    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=tester.index,
        y=tester['Adj Close'],
        name='Close Price'
    ))

    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=tester['Position Date'],
            y=tester['Adj Close'],
            name='FCA Shorts',
            hovertext=tester["Position Holder"],
            marker = dict(
                symbol="triangle-down",
                color='rgba(255, 0, 0, 0.9)',
                size=15

            )))

    tester.reset_index(inplace=True)
    print(tester)
    inital_range = validrangefinder(tester, 'Adj Close', 'index')
    fig['layout']['xaxis'].update(range=inital_range)

    return fig






