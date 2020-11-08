import dash_html_components as html
import dash_bootstrap_components as dbc
from backend.navbar import navbar


DCF_card_content = [
    dbc.CardHeader("DCF Estimation"),
    dbc.CardImg(src="../assets/images/cash-flow.svg", top=True, title="Icon made by Eucalyp from www.flaticon.com", className="card-img"),
    dbc.CardBody(
        [
            html.P(
                "Historical estimation of an intrinsic value for all S&P500 companies "
                "using discounted cash flows (DCF) analysis",
                className="card-text",
            ),
        dbc.Button("DCF", color="primary", href="/DCF")
        ]
    ),
]

PE_card_content = [
    dbc.CardHeader("P/E Ratio"),
    dbc.CardImg(src="../assets/images/calculator.svg", top=True, title="Icon made by Good Ware from www.flaticon.com", className="card-img"),
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
    dbc.CardImg(src="../assets/images/factory.svg", top=True, title="Icon made by srip from www.flaticon.com", className="card-img"),
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

FCA_card_content = [
    dbc.CardHeader("FCA Short Analyser"),
    dbc.CardImg(src="../assets/images/short.svg", top=True, title="Icon made by Freepik from www.flaticon.com", className="card-img"),
    dbc.CardBody(
        [
                        html.P(
                "Analysis of FCA short declerations for publically listed companies in the UK. Includes entry and exit points aswell "
                "as performance analysis of managers shorts",
                className="card-text",
            ),
        dbc.Button("FCA Short Analyser", color="primary", href="/FCA-Short")
        ]
    ),
]

valuable_market_monitors = [
    dbc.CardHeader("Market Monitors"),
    dbc.CardImg(src="../assets/images/market-monitor.svg", top=True, title="Icon made by Freepik from www.flaticon.com", className="card-img"),
    dbc.CardBody(
        [
                        html.P(
                "Popular, but sometimes under-represented metrics including Shiller CAPE and the Buffet Indicator ",
                className="card-text",
            ),
        dbc.Button("Market Monitors", color="primary", href="/market-monitors")
        ]
    ),
]

Basic_Algo = [
    dbc.CardHeader("Basic Algorithm"),
    dbc.CardImg(src="../assets/images/algorithm.svg", top=True, title="Icon made by Smashicons from www.flaticon.com", className="card-img"),
    dbc.CardBody(
        [
                        html.P(
                "Basic algorithm with transparent parameters and full historic performance",
                className="card-text",
            ),
        dbc.Button("Algorithm", color="primary", href="/algo")
        ]
    ),
]

padding = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("")))])

upper_card_deck = dbc.CardDeck([dbc.Card(PE_card_content),dbc.Card(DCF_card_content),dbc.Card(PB_card_content)], style={'margin':20})
lower_card_deck = dbc.CardDeck([dbc.Card(FCA_card_content),dbc.Card(valuable_market_monitors),dbc.Card(Basic_Algo)], style={'margin':20})
#lower_card_deck =
layout = html.Div([navbar,padding,upper_card_deck, lower_card_deck])







