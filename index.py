import dash, dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from apps import landingpage, PEInteractive, dcfInteractive
from assets import dcfdraft
from app import app
from backend.navbar import navbar


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


dcf_page_layout = html.Div([navbar, html.H1('DCF')])
PE_page_layout = html.Div([navbar, html.H1('PE')])
PB_page_layout = html.Div([navbar, html.H1('PB')])

# Update the index
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/DCF':
        return dcfInteractive.layout
    elif pathname == '/PE':
        return PEInteractive.layout
    elif pathname == '/PB':
        return PB_page_layout
    else:
        return landingpage.layout

if __name__ == '__main__':
    app.run_server(debug=True, port=8888)