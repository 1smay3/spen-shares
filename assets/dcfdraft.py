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
#App
from app import app

#Generate df for plotting
dfWide= pd.read_csv(r'C:/Users/spenc/PycharmProjects/spen-shares/data/DCF/MMM_HDCF.csv')

#Create list of stocks for dropdown

def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

StockDCFfig = stockpriceDCFplot(" Daily Price and DCF", dfWide, 'MMM')
ChangeFig = deviationPlot("DCF Deviation from Stock Price", dfWide)

# Define the app
charts = html.Div(
    children=[
        html.Div(
                 children=[
                     # Change class to change coloumns
                    html.Div(
                             children=[
                                 html.H2('Spen Shares - DCF'),
                                 html.P('Visualising DCF estimation series'),
                                 html.P('Pick stocks from the dropdown below.'),
                                 html.Div(

                                     children=[
                                         dcc.Dropdown(id='stockselector', options=getspydictionary(),
                                                      multi=False, value='MMM',
                                                      style={'backgroundColor': '#1E1E1E'},

                                                      ),
                                     ],
                                     style={'color': '#1E1E1E'})
                                ]
                             ),
                    html.Div(
                             children=[
                                 dcc.Graph(id='PricesChart', figure=StockDCFfig),
                                 dcc.Graph(id= 'DCFChart', figure=ChangeFig)

                             ])
                              ])
        ]

)
layout = html.Div([navbar, charts])

# # Update price chart
# @app.callback(
#     dash.dependencies.Output('PricesChart', 'figure'),
#     [dash.dependencies.Input('stockselector', 'value')])
#
# def update_chart(value):
#     companySelected = value
#     newDF = pd.read_csv(r"C:/Users/spenc/PycharmProjects/spen-shares/data/DCF/" + companySelected + "_HDCF.csv")
#     figure = stockpriceDCFplot(" Daily Price and DCF", newDF, companySelected)
#     return figure
#
# # Update deviation chart
# @app.callback(
#     dash.dependencies.Output('DCFChart', 'figure'),
#     [dash.dependencies.Input('stockselector', 'value')])
#
# def update_chart(value):
#     companySelected = value
#     newDF = pd.read_csv(r"C:/Users/spenc/PycharmProjects/spen-shares/data/DCF/" + companySelected + "_HDCF.csv")
#     figure = deviationPlot("DCF Deviation from Stock Price", newDF)
#     return figure
