### Dash
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

#Functions
from backend.chartplotter import *
from backend.SPYConstituents import *
from backend.navbar import navbar
import pickle
#App
from app import app


#Define parts of page
# Dropdown Selector
FirmSelector = html.Div(
                             children=[
                                 html.H2('DCF Estimation'),
                                 html.P('Visualising DCF estimation series'),
                                 html.P('Pick stocks from the dropdown below to update the charts.'),
                                 html.Div(

    dcc.Dropdown(id='stockselector', options=getspydictionary(),
                                                      multi=False, value='MMM'
                                                            )
                                 )])

# Make PE charts

#Generate df for plotting and drop index to allow easier charting
dfWide= pd.read_csv(r'C:/Users/spenc/PycharmProjects/spen-shares/data/DCF/MMM_HDCF.csv')

#Create list of stocks for dropdown

def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

#plot charts
StockDCFfig = stockpriceDCFplot(" Daily Price and DCF", dfWide, 'MMM')
ChangeFig = deviationPlot("DCF Deviation from Stock Price", dfWide)

topChart = html.Div(className="dashboard-chart",
    children=[
        dcc.Graph(id='PricesChart', figure=StockDCFfig)


    ])

bottomchart = html.Div(className="dashboard-chart",
    children=[
        dcc.Graph(id='DCFChart', figure=ChangeFig)


    ])


# EXTRACTED LAYOUT VERSION - CONDENSE WITH ASSIGNMENTS ABOVE LATER

layout = [navbar,html.Div(
    [
        dbc.Row(
            [
                dbc.Col(FirmSelector, width=2, className='dashboard-LHS-columns'),
                dbc.Col([
                    html.Div(dbc.Row(topChart)),
                    html.Div(dbc.Row(bottomchart))
                    ], width=10, className='dashboard-RHS-columns'

                )]
        )])]


# Update price chart
@app.callback(
    dash.dependencies.Output('PricesChart', 'figure'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_chart(value):
    companySelected = value
    newDF = pd.read_csv(r"C:/Users/spenc/PycharmProjects/spen-shares/data/DCF/" + companySelected + "_HDCF.csv")
    figure = stockpriceDCFplot(" Daily Price and DCF", newDF, companySelected)
    return figure

# Update deviation chart
@app.callback(
    dash.dependencies.Output('DCFChart', 'figure'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_chart(value):
    companySelected = value
    newDF = pd.read_csv(r"C:/Users/spenc/PycharmProjects/spen-shares/data/DCF/" + companySelected + "_HDCF.csv")
    figure = deviationPlot("DCF Deviation from Stock Price", newDF)
    return figure
















