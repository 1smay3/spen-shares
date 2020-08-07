import dash_bootstrap_components as dbc
import pandas as pd
import glob
import os
from settings import DATA_ROOT
import dash_html_components as html
from navbar import navbar

list_of_files = glob.glob(DATA_ROOT + '/FCA/*.csv') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

FCAShortsDF = pd.read_csv(latest_file)

table = dbc.Table.from_dataframe(FCAShortsDF, striped=True, bordered=True, hover=True)

layout = html.Div([navbar,table])