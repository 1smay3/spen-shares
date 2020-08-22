#
# import pandas as pd
# import glob
# import os
# from settings import DATA_ROOT
# import dash_html_components as html
#
# import re
#
# from backend.FCAShort import getFCAdictionary, getISIN
# from backend.FCAPlot import FCAPlot
# from app import app
# from backend.navbar import navbar
# import dash
# import dash_core_components as dcc
# import dash_bootstrap_components as dbc
#
#
#
# list_of_files = glob.glob(DATA_ROOT + '/FCA/*.csv') # * means all if need specific format then *.csv
# latest_file = max(list_of_files, key=os.path.getctime)
#
# # Get latest date for update token
# end_of_file_name= re.findall('^[^_]+_([^_]+)',latest_file)
# #Convert to string
# file_name_string = ''.join(end_of_file_name)
# #Get slice of 10 char to get date
# latest_update_date = file_name_string[:10]
#
# # Dropdown Selector
# FirmSelector = html.Div(
#                              children=[
#                                  html.H2('DCF Estimation'),
#                                  html.P('Visualising DCF estimation series'),
#                                  html.P('Pick stocks from the dropdown below to update the charts.'),
#                                  html.P('Data as of: ' + latest_update_date),
#                                  html.Div(
#
#     dcc.Dropdown(id='firmselector', options=getFCAdictionary(),
#                                                       multi=False, value='GB00B5N0P849'
#
#                                                             )
#                                  )
#                              ])
#
# #plot charts
# MainChart = FCAPlot("GB00B5N0P849")
#
#
#
# FCAChart = html.Div(className="dashboard-chart",
#     children=[
#         dcc.Graph(id='FCAChart', figure=MainChart)
#     ])
#
#
#
# # Update price chart
# @app.callback(
#     dash.dependencies.Output('FCAChart', 'figure'),
#     [dash.dependencies.Input('firmselector', 'value')])
#
# def update_chart(value):
#     #Convert name to ISIN
#     print(value)
#     figure = FCAPlot(value)
#     return figure
#
#
#
# layout = [navbar,html.Div(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(FirmSelector, width=2, className='dashboard-LHS-columns'),
#                 dbc.Col([
#                     html.Div(dbc.Row(FCAChart)),
#                     ], width=10, className='dashboard-RHS-columns'
#
#                 )]
#         )])]
