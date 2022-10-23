# keywords/tags for grocery vendors
grocer = ['ralphs', 'sayweee', 'amazon']

# in case first scrape yields invalid result
attempt = 0

# headers for using requests
cred = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'}

#functional programing in Google Sheets
top = '=ifs(isna(match(min(K2:M2),K2,0))=FALSE,"Ralphs",isna(match(min(K2:M2),L2,0))=FALSE,"Weee!",isna(match(min(K2:M2),M2,0))=FALSE,"Amazon Fresh")'
# parse this string, index of K at first '...K2' is at 20, second at 64, third at 107
# '...K2:M2),K2_...' index of _is at                   29,           73           116
p = [top[:20], top[29:64], top[73:107], top[116:]]
col = ["K", "L", "M"]

# dataframe indices
item = "item(name)"
cheapest = "Best pick:"
link_labels = ["link(Ralph's)", "link(Weee!)", "link(AZFresh)"]
raw_cost_labels = ["rcost(Ralph's)", "rcost(Weee!)", "rcost(AZFresh)"]
divisor_labels = ["divisor(Ralph's)", "divisor(Weee!)", "divisor(AZFresh)"]
price_labels = ["price(Ralph's)", "price(Weee!)", "price(AZFresh)"]

# test urls to update dummy sheet on Google Spreadshets
test_urls = ["https://www.ralphs.com/p/russet-potatoes/0003338353010?fulfillment=PICKUP&searchType=default_search", 
"https://www.sayweee.com/en/product/Barilla-Spaghetti-Pasta/47727",
"https://www.amazon.com/365-Everyday-Value-Organic-Capellini/dp/B074H6X463/",
"https://www.ralphs.com/p/banana/0000000004011?fulfillment=PICKUP",
"https://www.amazon.com/Amazon-Brand-Happy-Belly-Cage-Free/dp/B071J311RT/",
"https://www.ralphs.com/p/medium-avocado/0000000004046?fulfillment=PICKUP",
"https://www.sayweee.com/en/product/Sakura-Ground-Pork--Frozen/23425?category=meat01",
"https://www.amazon.com/Amazon-Brand-Happy-Previously-Solimo/dp/B07X2SQ332/"]