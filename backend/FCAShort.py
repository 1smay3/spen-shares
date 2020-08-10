import pandas as pd
import requests
from pandas.tseries.offsets import BDay
import time
from backend.YahooAPI import *

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
CurrentSheetList = list(s for s in raw_shorts_sheetnames if CurrentDisclosures in s)
HistoricalSheetList = list(s for s in raw_shorts_sheetnames if HistoricalDisclosures in s)

# Load into dataframe
CurrentDisclosuresExcel = pd.read_excel(data_request, sheet_name=CurrentSheetList[0])

# Refine current disclosures
CurrentDisclosuresReindexed = CurrentDisclosuresExcel.set_index('Name of Share Issuer')

# Group by firm which is being shorted, and sum to see total short exposure
SummedShortDuplicates = CurrentDisclosuresReindexed.groupby(['Name of Share Issuer'])['Net Short Position (%)'].transform('sum')

# The above transformations turns it into a series, so change back to df
SummedShortDuplicatesDF = pd.DataFrame(SummedShortDuplicates, index=CurrentDisclosuresExcel['Name of Share Issuer'])

# Delete duplicates as summing process keeps all share issuer entries
SummedShortDF = SummedShortDuplicatesDF.drop_duplicates()
SummedShortDFSorted = SummedShortDF.sort_values(by=['Net Short Position (%)'], ascending=False)

# Get list of stocks firms are currently long
CurrentDisclosuresList = CurrentDisclosuresExcel['ISIN'].to_list()

#Remove duplicates
CurrentDisclosuresList = (list(set(CurrentDisclosuresList)))

# Make a dataframe for each relevant ISIN
for ISIN in CurrentDisclosuresList:
    dfName = ISIN + "df"
    dfName = CurrentDisclosuresExcel.loc[CurrentDisclosuresExcel['ISIN'] == ISIN]
    earliest_date = dfName['Position Date'].min()
    latest_date = dfName['Position Date'].max()
    #Subtract 1 year working days from the date and add to end. If date is in future it just gets the most it can
    earliest_date = (earliest_date - BDay(252)).date()
    latest_date = (latest_date + BDay(252)).date()

    dfName.to_pickle("C:/Users/spenc/PycharmProjects/spen-shares/data/FCAData/" + str(ISIN) + "_HFCA.pkl")
    # Download data from yahoo and save. Then sleep to prevent cooldown
    try:
        relevant_prices = YahooStockPrice(ISIN, earliest_date, latest_date)
        # Save down relevant prices
        relevant_prices.to_pickle("C:/Users/spenc/PycharmProjects/spen-shares/data/YAHOOPRICES/" + str(ISIN) + "_HPRI.pkl")
        print(relevant_prices)
        time.sleep(1)
    except AttributeError:
        pass


# Use sheetname as filename suffix
# save_down = DATA_ROOT+"/FCA/FCASHORTS_"+str(CurrentSheetList.replace('.', '-'))+".csv"
# SummedShortDFSorted.to_csv(save_down)
