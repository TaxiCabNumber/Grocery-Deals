import get_data as g
import best_pick as b
import constants as c
import pygsheets as pygs
import pandas as pd

#authorization
gc = pygs.authorize(service_file='/Users\joncc\Documents\Personal Projects\grocery-deals-service-key.json')

#open the google spreadsheet
sh = gc.open('Grocery Deals')
wks_list = sh.worksheets() #creates a list of worksheet objects

#look at the first three sheets
for j in range(3):
    wks = sh.worksheet('index', j) #select jth sheet
    df = pd.DataFrame() # Create empty dataframe per sheet
    df = wks.get_as_df() #convert whole sheet to df
    print("Working on", wks_list[j].title, "sheet ---------------------------")
    for i in df.index:
        for k in range(3): #terate through the domains
            url = df[c.link_labels[k]].iat[i] 
            tag = g.get_data(url)
            print(df[c.item].iat[i], "costs $", tag) #visualize cost
            df[c.raw_cost_labels[k]].iat[i] = tag
            if type(tag) == str:
                df[c.price_labels[k]].iat[i] = float(tag)/float(df[c.divisor_labels[k]].iat[i]) #unit price
            else:
                df[c.price_labels[k]].iat[i] = "n/a" #no price found
            #use index i as input for best pick, since we are going row by row
            df[c.cheapest].iat[i] = b.best_pick(i) 
        #update each line with df, starting at cell (i, j). 
        wks.set_dataframe(df,(1,1))


#implementation
##for each page sh[j], select 3 separate columns for AZF, Ralph, and Weee and store into df
##after each df is populated, go down the df and access the link
#### parse the url, make define keyword/tag based on domain --> feed into function
##webscrape the page looking for a key phrase and store that price variable in the 2nd column of respective df
#select the second column of each df and write to the spreadsheet