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
                                 html.H2('Historical P/B Ratio'),
                                 html.P('Visualising P/B Ratio and its relationship to price'),
                                 html.P('Pick stocks from the dropdown below to update the charts.'),
                                 html.Div(

    dcc.Dropdown(id='stockselector', options=getspydictionary(),
                                                      multi=False, value='MMM'
                                                            )
                                 )])

# Make PE charts

#Generate df for plotting and drop index to allow easier charting
priceBookDF = pd.read_csv(DATA_ROOT + '/PBRATIO/MMM_HPB.csv')



#Create list of stocks for dropdown

def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

#plot charts
StockPBfig = stockPB_PRICEplot(" Daily Price and P/B Ratio", priceBookDF, 'MMM')
TATLSHEchart = stockCACLPICEplot(" Total Asset, Liabilities & Shareholders Equity", priceBookDF, 'MMM')

topChart = html.Div(className="dashboard-chart",
    children=[
        dcc.Graph(id='PB Chart', figure=StockPBfig)


    ])

bottomchart = html.Div(className="dashboard-chart",
    children=[
        dcc.Graph(id='TATLSHE Chart', figure=TATLSHEchart)


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
    dash.dependencies.Output('PB Chart', 'figure'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_chart(value):
    companySelected = value
    newDF = pd.read_csv(DATA_ROOT + "/PBRATIO/" + companySelected + "_HPB.csv")
    figure = stockPB_PRICEplot(" Daily Price and P/B Ratio", newDF, companySelected)
    return figure

# Update deviation chart
@app.callback(
    dash.dependencies.Output('TATLSHE Chart', 'figure'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_chart(value):
    companySelected = value
    newDF = pd.read_csv(DATA_ROOT + "/PBRATIO/" + companySelected + "_HPB.csv")
    figure = stockCACLPICEplot("Total Assets, Liabilities & Shareholders Equity", newDF, companySelected)
    return figure
















