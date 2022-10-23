import get_data as g
import pygsheets as pygs
import pandas as pd

#authorization
gc = pygs.authorize(service_file='/Users\joncc\Documents\Personal Projects\grocery-deals-service-key.json')

# Create empty dataframe
df = pd.DataFrame()

#open the google spreadsheet
sh = gc.open('Grocery Deals')

#select the test sheet 
wks = sh[3]


#read current sheet
df = wks.get_as_df() #convert whole sheet to df
print(df['Link']) #visualize links visited

i = 0 #set to length of column
for i in df.index:
    url = df["Link"].iat[i] #first entry
    tag = g.get_data(url)
    print(tag)
    df["Price"].iat[i] = tag

#update the first sheet with df, starting at cell (i, j). 
wks.set_dataframe(df,(1,1))


#implementation
#for each page sh[j], select 3 separate columns for AZF, Ralph, and Weee and store into df
#after each df is populated, go down the df and access the link
### parse the url, make define keyword/tag based on domain --> feed into function
#webscrape the page looking for a key phrase and store that price variable in the 2nd column of respective df
#select the second column of each df and write to the spreadsheet