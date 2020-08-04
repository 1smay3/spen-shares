import dash_html_components as html
import dash_bootstrap_components as dbc
from backend.navbar import navbar


DCF_card_content = [
    dbc.CardHeader("DCF Estimation"),
    dbc.CardImg(src="../assets/cash-flow.svg", top=True, title="Icon made by Eucalyp from www.flaticon.com", className="card-img"),
    dbc.CardBody(
        [
            html.P(
                "Some quick example text to build on the card title and "
                "make up the bulk of the card's content.",
                className="card-text",
            ),
        dbc.Button("DCF", color="primary", href="/DCF")
        ]
    ),
]

PE_card_content = [
    dbc.CardHeader("P/E Ratio"),
    dbc.CardImg(src="../assets/calculator.svg", top=True, title="Icon made by Good Ware from www.flaticon.com", className="card-img"),
    dbc.CardBody(
        [
            html.P(
                "Historical P/E ratio for all S&P500 companies",
                className="card-text",
            ),
        dbc.Button("P/E Ratio", color="primary", href="/PE")
        ]
    ),
]

PB_card_content = [
    dbc.CardHeader("P/B Ratio"),
    dbc.CardImg(src="../assets/factory.svg", top=True, title="Icon made by srip from www.flaticon.com", className="card-img"),
    dbc.CardBody(
        [
                        html.P(
                "Historical P/B ratio for all S&P500 companies",
                className="card-text",
            ),
        dbc.Button("P/B Ratio", color="primary", href="/PB")
        ]
    ),
]

padding = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("")))])

card_deck = dbc.CardDeck([dbc.Card(PE_card_content),dbc.Card(DCF_card_content),dbc.Card(PB_card_content)], style={'margin':20})

layout = html.Div([navbar,padding,card_deck])







