from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as bp
import constants as c

url = "https://www.ralphs.com/p/russet-potatoes/0003338353010?"
#url = "https://www.sayweee.com/en/product/Barilla-Spaghetti-Pasta/47727"
url = "https://www.amazon.com/365-Everyday-Value-Organic-Capellini/dp/B074H6X463/"



# implement inheritance/polymorphism to distinguish b/t Weee and AZF, which both utilize requests
# all functions inherit domain()
# set a keyword 'weee' as an input to call polymorph on the non-HTMLSession variant

def getData(url):
    tag = '' #initialize as empty string
    d = domain(url)
    #switch statement for domain of URL --> different keyword (store in constants.py)
    #ralphs
    if d == c.grocer[0]: 
        s = HTMLSession() #for some reason cannot use requests for ralphs
        r = s.get(url)
        ralph = bp(r.text, 'html.parser')
        tag = ralph.find("data", class_= "kds-Price kds-Price--alternate mb-8").get("value") # tag may change based on a strikethrough indicating discount
        #tag = doc.data.get("value")  #also returns same value
        #print(tag) #debug
    #weee
    elif d == c.grocer[1]:
        w = requests.get(url, headers= c.cred)
        weee = bp(w.content, 'lxml')
        tag = weee.find("div", class_= "Header_price_price__4mkmc").get_text() # tag may change based on a strikethrough indicating discount
        if tag != None and tag.find("$") != -1: #check type before calling str function
            j = tag.find("$")
            tag = tag[j+1:] #omit $ sign
        #print(tag)
    #amazonfresh
    elif d == c.grocer[2]:
        page = requests.get(url, headers= c.cred)
        doc = bp(page.content, 'lxml')
        tag = doc.find('span', attrs={"id":'priceblock_ourprice'}).get_text() 
    if tag == None or tag == '':
        return "no change" #keyword to not modify the entry in sheet df
    else:
        return tag # can be none nonetype

def domain(url):
    for n in c.grocer:
        d = url.find(n, 12) # ignore "https://www."
        if d == 12:
            return n
    # now we know our domain from the url
    
tag = getData(url)
print(tag)