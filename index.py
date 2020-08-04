### Dash
import dash, dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
# Apps and app
from apps import LandingPage, PEInteractive, DCFInteractive
from app import app
from app import server

# Navbar
from backend.navbar import navbar

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

PB_page_layout = html.Div([navbar, html.H1('PB')])

# Update the index
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/DCF':
        return DCFInteractive.layout
    elif pathname == '/PE':
        return PEInteractive.layout
    elif pathname == '/PB':
        return PB_page_layout
    else:
        return LandingPage.layout

if __name__ == '__main__':
    app.run_server(debug=True, port=8888)