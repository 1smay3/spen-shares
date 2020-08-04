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
                                                      multi=False, value='MMM',
                                                            className='dashboard-LHS-columns')
                                 )])

# Make PE charts

#Generate df for plotting and drop index to allow easier charting
priceEarningsDF= pd.read_pickle(r'C:/Users/spenc/PycharmProjects/spen-shares/data/PERATIO/MMM.pkl')
priceEarningsDF.reset_index(inplace=True)

#Create list of stocks for dropdown

def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

#plot charts
StockPEfig = stockPEPRICEplot(" Daily Price and P/E Ratio", priceEarningsDF, 'MMM')
EPSfig = stockEPSplot(" Daily Price and P/E Ratio", priceEarningsDF, 'MMM')

topChart = html.Div(
    children=[
        dcc.Graph(id='PE Chart', figure=StockPEfig)


    ])

bottomchart = html.Div(
    children=[
        dcc.Graph(id='PE Chart', figure=EPSfig)


    ])


# EXTRACTED LAYOUT VERSION - CONDENSE WITH ASSIGNMENTS ABOVE LATER

layout2 = [navbar,
          dbc.Col(FirmSelector),
          html.Div(dbc.Col(topChart))]

working_base_layout = [navbar,html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div("One of two columns"), width=4),
                dbc.Col([
                    html.Div(dbc.Row("One of row in columns")),
                    html.Div(dbc.Row("One of row in columns"))]
                )]
        )])]




























