import dash, dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from apps import home

BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#Simple Navbar cant have logo. Leave that for now.



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/Home"), id="Home-link"),
        dbc.NavItem(dbc.NavLink("DCF", href="/DCF"), id="DCF-link"),
        dbc.NavItem(dbc.NavLink("PE", href="/PE"), id="PE-link"),
        dbc.NavItem(dbc.NavLink("PB", href="/PB"), id="PB-link")

    ],
    brand="SpenShares",
    brand_href="/",
    color="primary",
    dark=True,
)

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
        return dcf_page_layout
    elif pathname == '/PE':
        return PE_page_layout
    elif pathname == '/PB':
        return PB_page_layout
    else:
        return home.layout
        # You could also return a 404 "URL not found" page here


# Update which link is active in the navbar
# If there's lots of pages, we can probably be cleverer about generating
# these functions dynamically.
#@app.callback(Output('page-1-link', 'active'), [Input('url', 'pathname')])
#def set_page_1_active(pathname):
    #return pathname == '/page-1'

#@app.callback(Output('page-2-link', 'active'), [Input('url', 'pathname')])
#def set_page_2_active(pathname):
    #return pathname == '/page-2'


if __name__ == '__main__':
    app.run_server(debug=True, port=8888)