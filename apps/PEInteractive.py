### Dash
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

#Functions
from backend.ChartPlotter import *
from backend.SPYGrab import *
from backend.navbar import navbar
#App
from app import app
from settings import DATA_ROOT

#Define parts of page
# Dropdown Selector
FirmSelector = html.Div(
                             children=[
                                 html.H2('Historical P/E Ratio'),
                                 html.P('Visualising P/E Ratio and its relationship to price'),
                                 html.P('Pick stocks from the dropdown below to update the charts.'),
                                 html.Div(

    dcc.Dropdown(id='stockselector', options=getspydictionary(),
                                                      multi=False, value='MMM'
                                                            )
                                 )])

# Make PE charts

#Generate df for plotting and drop index to allow easier charting
priceEarningsDF= pd.read_pickle(DATA_ROOT + '/PERATIO/MMM.pkl')
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

topChart = html.Div(className="dashboard-chart",
    children=[
        dcc.Graph(id='PE Chart', figure=StockPEfig)


    ])

bottomchart = html.Div(className="dashboard-chart",
    children=[
        dcc.Graph(id='EPS Chart', figure=EPSfig)


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
    dash.dependencies.Output('PE Chart', 'figure'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_chart(value):
    companySelected = value
    newDF = pd.read_pickle(DATA_ROOT + "/PERATIO/" + companySelected + ".pkl")
    newDF.reset_index(inplace=True)
    figure = stockPEPRICEplot(" Daily Price and P/E Ratio", newDF, companySelected)
    return figure

# Update deviation chart
@app.callback(
    dash.dependencies.Output('EPS Chart', 'figure'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_chart(value):
    companySelected = value
    newDF = pd.read_pickle(DATA_ROOT + "/PERATIO/" + companySelected + ".pkl")
    newDF.reset_index(inplace=True)
    figure = stockEPSplot("Daily Earnings Per Share (EPS)", newDF, companySelected)
    return figure
















