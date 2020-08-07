### Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# Apps and components
from apps import LandingPage, PEInteractive, DCFInteractive, PBInteractive
from app import app
from app import server

# Navbar
from backend.navbar import navbar

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

PB_page_layout = html.Div([navbar, html.H1('Work In Progress - PB')])
FCA_page_layout = html.Div([navbar, html.H1('Work In Progress - FCA')])
MarketMonitor_page_layout = html.Div([navbar, html.H1('Work In Progress - MM')])
Algo_page_layout = html.Div([navbar, html.H1('Work In Progress - ALGO')])


# Update the index
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/DCF':
        return DCFInteractive.layout
    elif pathname == '/PE':
        return PEInteractive.layout
    elif pathname == '/PB':
        return PBInteractive.layout
    elif pathname == '/market-monitors':
        return MarketMonitor_page_layout
    elif pathname == '/FCA-Short':
        return FCA_page_layout
    elif pathname == '/algo':
        return Algo_page_layout
    else:
        return LandingPage.layout

if __name__ == '__main__':
    app.run_server(debug=True, port=8888)