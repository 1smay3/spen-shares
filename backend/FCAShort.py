import pandas as pd
from settings import DATA_ROOT
import requests
import re
# Use request otherwise get HTTP 403 error

url = "https://www.fca.org.uk/publication/data/short-positions-daily-update.xls"
data_request = requests.get(url).content

# Just take first sheet as newest data
raw_shorts = pd.ExcelFile(data_request)
raw_shorts_sheetnames = raw_shorts.sheet_names

# Dataframe current exposure
CurrentDisclosures = "Current Disclosures"
HistoricalDisclosures="Historical Disclosures"

# Convert to list to be data and not where it is located in physical memory. [0] Gets first value in list, should be only value
# unless FCA change.
CurrentSheetList = list(s for s in raw_shorts_sheetnames if CurrentDisclosures in s)[0]
HistoricalSheetList = list(s for s in raw_shorts_sheetnames if HistoricalDisclosures in s)[0]

# Load into dataframe
CurrentDisclosuresExcel = pd.read_excel(data_request, sheet_name=CurrentSheetList)

# Refine current disclosures
CurrentDisclosuresReindexed = CurrentDisclosuresExcel.set_index('Name of Share Issuer')

# Group by firm which is being shorted, and sum to see total short exposure
SummedShortDuplicates = CurrentDisclosuresReindexed.groupby(['Name of Share Issuer'])['Net Short Position (%)'].transform('sum')

# The above transformations turns it into a series, so change back to df
SummedShortDuplicatesDF = pd.DataFrame(SummedShortDuplicates, index=CurrentDisclosuresExcel['Name of Share Issuer'])

# Delete duplicates as summing process keeps all share issuer entries
SummedShortDF = SummedShortDuplicatesDF.drop_duplicates()
SummedShortDFSorted = SummedShortDF.sort_values(by=['Net Short Position (%)'], ascending=False)

# Use sheetname as filename suffix

save_down = DATA_ROOT+"/FCA/FCASHORTS_"+str(CurrentSheetList.replace('.', '-'))+".csv"
SummedShortDFSorted.to_csv(save_down)


#
# today = datetime.datetime.today()
# # Working day offset
# offset = max(1, (today.weekday() + 6) % 7 - 3)
#
# timedelta = datetime.timedelta(offset)
# most_recent = today #- timedelta
#
# relevant_date = most_recent.strftime('%d.%m.%Y')
#
# first_sheet = str(relevant_date) + " Current Disclosures "
#
#
#
#
#
#



