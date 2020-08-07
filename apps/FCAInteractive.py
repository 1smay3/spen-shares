import dash_bootstrap_components as dbc
import pandas as pd
import glob
import os
from settings import DATA_ROOT
import dash_html_components as html
from backend.navbar import navbar
import re


list_of_files = glob.glob(DATA_ROOT + '/FCA/*.csv') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

# Get latest date for update token
end_of_file_name= re.findall('^[^_]+_([^_]+)',latest_file)
#Convert to string
file_name_string = ''.join(end_of_file_name)
#Get slice of 10 char to get date
latest_update_date = file_name_string[:10]

# Update badge - this can be removed when its mad so its always newest data
badge = dbc.Button(
    ["Data as of: " + latest_update_date, dbc.Badge(color="light", className="ml-1")],
    color="primary",
)



#Generate table
FCAShortsDF = pd.read_csv(latest_file)
table = dbc.Table.from_dataframe(FCAShortsDF, striped=True, bordered=True, hover=True)

# Form layout to be called
layout = html.Div([navbar,badge, table])