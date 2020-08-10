from data.YAHOOPRICES import *
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px


# TEST WITH ISIN

def FCAPlot(ISIN):
    #Import Prices
    ISIN_Prices = pd.read_pickle("C:/Users/spenc/PycharmProjects/spen-shares/data/YAHOOPRICES/" + str(ISIN) + "_HPRI.pkl")
    ISIN_Shorts = pd.read_pickle("C:/Users/spenc/PycharmProjects/spen-shares/data/FCAData/" + str(ISIN) + "_HFCA.pkl")

    # Add price to end of isin short


    #Reindex to date
    ISIN_Shorts.set_index(ISIN_Shorts['Position Date'], inplace=True)
    print(ISIN_Shorts)

    tester = pd.concat([ISIN_Prices, ISIN_Shorts], axis=1)

    print(tester.tail(20))
    print(ISIN_Shorts)

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





    fig.show()




    # fig.show()



FCAPlot("GB00BZ1G4322")