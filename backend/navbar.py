import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/Home"), id="Home-link"),
        dbc.NavItem(dbc.NavLink("PE", href="/PE"), id="PE-link"),
        dbc.NavItem(dbc.NavLink("DCF", href="/DCF"), id="DCF-link"),
        dbc.NavItem(dbc.NavLink("PB", href="/PB"), id="PB-link"),
        dbc.NavItem(dbc.NavLink("FCA Shorts", href="/FCA-Short"), id="PB-link"),
        dbc.NavItem(dbc.NavLink("Market Monitors", href="/market-monitors"), id="MM-link"),
        dbc.NavItem(dbc.NavLink("Algorithm", href="/algo"), id="algo-link")


    ],
    brand="SpenShares",
    brand_href="/home",
    color="secondary",
    dark=True,
    fluid=True
)
