import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/Home"), id="Home-link"),
        dbc.NavItem(dbc.NavLink("DCF", href="/DCF"), id="DCF-link"),
        dbc.NavItem(dbc.NavLink("PE", href="/PE"), id="PE-link"),
        dbc.NavItem(dbc.NavLink("PB", href="/PB"), id="PB-link")

    ],
    brand="SpenShares",
    brand_href="/home",
    color="primary",
    dark=True,
)
