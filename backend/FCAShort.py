import pandas as pd
from settings import DATA_ROOT
import requests
import datetime
# Use request otherwise get HTTP 403 error

url = "https://www.fca.org.uk/publication/data/short-positions-daily-update.xls"
req = requests.get(url).content

# Sheet name is variable, changing everyday to include the most recent update date.
# Hence, pass as variable.

today = datetime.datetime.today()
# Working day offset
offset = max(1, (today.weekday() + 6) % 7 - 3)

timedelta = datetime.timedelta(offset)
most_recent = today #- timedelta

relevant_date = most_recent.strftime('%d.%m.%Y')

first_sheet = str(relevant_date) + " Current Disclosures "

raw_shorts = pd.read_excel(req)
raw_shorts_reindexed = raw_shorts.set_index('Name of Share Issuer')


#Group by firm which is being shorted, and sum to see total short exposure
summed_short_duplicates = raw_shorts_reindexed.groupby(['Name of Share Issuer'])['Net Short Position (%)'].transform('sum')
#The above transformations turns it into a series, so change back to df
ssd_df = pd.DataFrame(summed_short_duplicates, index=raw_shorts['Name of Share Issuer'])
#Delete duplicates as summing process keeps all share issuer entries
summed_short = ssd_df.drop_duplicates()
summed_short_sorted = summed_short.sort_values(by=['Net Short Position (%)'], ascending=False)
#Change . in date to - so windows doesnt think its a filetype
save_down = DATA_ROOT+"/FCA/FCASHORTS_"+str(relevant_date.replace('.', '-'))+".csv"
summed_short_sorted.to_csv(save_down)
