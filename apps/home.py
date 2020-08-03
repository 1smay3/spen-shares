import dash_html_components as html
import dash_bootstrap_components as dbc
from index import navbar
# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
# change to app.layout if running as single page app instead

#get svg not png


DCF_card_content = dbc.Card(
    [
        dbc.CardHeader("DCF Estimation"),
        dbc.CardImg(src="/assets/money.png", top=True, title="ADD CREDIT COMMENT", className="card-img"),
        dbc.CardBody(
            [
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
            dbc.Button("DCF", color="primary"),
            ]
        ),
    ],
)

PE_card_content = [
    dbc.CardHeader("P/E Ratio"),
    dbc.CardBody(
        [
            dbc.CardImg(src="/assets/money.png", top=True, title="ADD CREDIT COMMENT", className="card-img"),
            html.P(
                "Historical P/E ratio for all S&P500 companies",
                className="card-text",
            ),
            dbc.Button("P/E Ratio", color="primary")
        ]
    ),
]

PB_card_content = [
    dbc.CardHeader("P/B Ratio"),
    dbc.CardBody(
        [
            dbc.CardImg(src="/assets/money.png", top=True, title="ADD CREDIT COMMENT", className="card-img"),
            html.P(
                "Historical P/B ratio for all S&P500 companies",
                className="card-text",
            ),
            dbc.Button("P/B Ratio", color="primary")
        ]
    ),
]


padding = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("")))], style={'padding': 10})

cards =dbc.Row(
            [
                dbc.Col(dbc.Card(PE_card_content, inverse=False), style={'margin': 10}),
                dbc.Col(dbc.Card(DCF_card_content, inverse=False), style={'margin': 10}),
                dbc.Col(dbc.Card(PB_card_content, inverse=False), style={'margin': 10}),
            ],
            className="mb-5",justify="center"
        )

layout = html.Div([navbar,padding,cards])







