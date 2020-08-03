import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

# Make default range that where there is data for DCF Deviaitoion
#button change color when clicked

def twoaxisplot(title, x_axis, LHS1_y_data, LHS2_y_data, RHS_y_data):

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])


    # Left hand side data 1
    fig.add_trace(
        go.Scatter(x=x_axis, y=LHS1_y_data, name="Close Price"),
        secondary_y=False,
    )
    # Left hand side data 2
    fig.add_trace(
        go.Scatter(x=x_axis, y=LHS2_y_data, name="DCF Estimation"),
        secondary_y=False,
    )
    # Right hand side data 2
    fig.add_trace(
        go.Scatter(x=x_axis, y=RHS_y_data, name="Deviation"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text=title,
        template='plotly_dark').update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    # Set x-axis title
    fig.update_xaxes(title_text="Date")

    # Add range slider and buttons
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all", label="All")
            ])
        )
    )

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Close Price / DCF ($)</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Deviation (%)</b>", secondary_y=True)

    # Auto Rescale y axis
    plt.autoscale(enable=True, tight=True)

    return fig

def stockpriceDCFplot(title, dataframe, ticker):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": False}]])

    # Left hand side data 1
    fig.add_trace(
        go.Scatter(x=dataframe['date'], y=dataframe[ticker], name="Close Price"),
        secondary_y=False,
    )
    # Left hand side data 2
    fig.add_trace(
        go.Scatter(x=dataframe['date'], y=dataframe['dcf'], name="DCF Estimation"),
        secondary_y=False,
    )

    # Add figure title
    fig.update_layout(
        title_text=title,
        template='plotly_dark').update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    #Show or Hide legend
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    # Set x-axis title
    fig.update_xaxes(title_text="Date")

    # Add range slider and buttons
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(bgcolor="#31302f", activecolor ="#46b650",
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all", label="All")
            ])
        )
    )

    # Update default range for valid data
    inital_range = validrangefinder(dataframe, 'dcf')
    fig['layout']['xaxis'].update(range=inital_range)

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Close Price / DCF ($)</b>", secondary_y=False)


    # Auto Rescale y axis
    plt.autoscale(enable=True, tight=True)

    return fig


def deviationPlot(title, dataframe):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": False}]])

    # Left hand side data 1
    fig.add_trace(
        go.Scatter(x=dataframe['date'], y=dataframe['Deviation'], name="DCF Deviation", marker_color='rgba(255, 255, 255, .9)'),
        secondary_y=False,
    )

    # Add figure title
    fig.update_layout(
        title_text=title,
        template='plotly_dark').update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    # Set x-axis title
    fig.update_xaxes(title_text="Date")



    # Add range slider and buttons
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(bgcolor="#31302f", activecolor ="#46b650",
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all", label="All")
            ])
        )
    )

    # Update default range for valid data
    inital_range = validrangefinder(dataframe, 'dcf')
    fig['layout']['xaxis'].update(range=inital_range)

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>DCF Estimation (%)</b>", secondary_y=False,tickformat=".1%")


    # Auto Rescale y axis
    plt.autoscale(enable=True, tight=True)

    return fig

def validrangefinder(dataframe, column):
    # Get initial range from DF and update defaul range accordingly
    firstValidPointIndex = dataframe.apply(pd.Series.first_valid_index)
    firstValidPointValues = dataframe.iloc[firstValidPointIndex[column]]
    specificFirstPoint = firstValidPointValues['date']

    lastValidPointIndex = dataframe.apply(pd.Series.last_valid_index)
    lastValidPointValues = dataframe.iloc[lastValidPointIndex[column]]
    specificlastPoint = lastValidPointValues['date']

    valid_range = [specificFirstPoint, specificlastPoint]

    return valid_range