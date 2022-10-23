from bs4 import BeautifulSoup as bp
import pygsheets
from requests_html import HTMLSession # workaround
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='/Users\joncc\Documents\Personal Projects\grocery-deals-service-key.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
#df['name'] = ['Onion', 'Carrot', 'Potato'] #dummy df

#open the google spreadsheet
sh = gc.open('Grocery Deals')

#select the test sheet 
wks = sh[4]

#read current sheet
df = wks.get_as_df() #convert whole sheet to df
print(df["Link"]) #visualize links visited

i = 0 #set to length of column
url = df["Link"].iat[i] #first entry

s = HTMLSession()

r = s.get(url)
doc = bp(r.text, 'html.parser')

tag = doc.find('data', class_= "kds-Price kds-Price--alternate mb-8") # tag may change based on a strikethrough indicating discount
tag = tag.get('value')
#tdata = doc.data.get_text()  #either works
#tdata = tag.get('value')
print(tag)
#print(type(tdata))


df["Price"] = [tag, "rand", "rand"]

#update the first sheet with df, starting at cell (i, j). 
wks.set_dataframe(df,(1,1))


#implementation
#for each page sh[j], select 3 separate columns for AZF, Ralph, and Weee and store into df
#after each df is populated, go down the df and access the link
### parse the url, make define keyword/tag based on domain --> feed into function
#webscrape the page looking for a key phrase and store that price variable in the 2nd column of respective df
#select the second column of each df and write to the spreadsheet