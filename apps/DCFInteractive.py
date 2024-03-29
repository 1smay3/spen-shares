### Dash
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import sys

#Functions
from backend.ChartPlotter import *
from backend.SPYGrab import *

# Directories
from settings import DATA_ROOT
#App and components
from app import app
from backend.navbar import navbar

#Generate df for plotting and drop index to allow easier charting
dfWide= pd.read_csv(DATA_ROOT + '/DCF/MMM_HDCF.csv')

#Get update date
data_update_date = dfWide['date'].iloc[-1]


#Define parts of page
# Dropdown Selector
FirmSelector = html.Div(
                             children=[
                                 html.H2('DCF Estimation'),
                                 html.P('Visualising DCF estimation series'),
                                 html.P('Pick stocks from the dropdown below to update the charts.'),
                                 html.P('Data as of: ' + data_update_date),
                                 html.Div(

    dcc.Dropdown(id='stockselector', options=getspydictionary(),
                                                      multi=False, value='MMM', clearable=False, className='selector'
                                                            )
                                 )
                             ])

# Make PE charts


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
    newDF = pd.read_csv(DATA_ROOT + "/DCF/" + companySelected + "_HDCF.csv")
    figure = stockpriceDCFplot(" Daily Price and DCF", newDF, companySelected)
    return figure

# Update deviation chart
@app.callback(
    dash.dependencies.Output('DCFChart', 'figure'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_chart(value):
    companySelected = value
    newDF = pd.read_csv(DATA_ROOT + "/DCF/" + companySelected + "_HDCF.csv")
    figure = deviationPlot("DCF Deviation from Stock Price", newDF)
    return figure
















