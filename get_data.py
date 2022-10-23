from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as bp
import constants as c

# implement inheritance/polymorphism to distinguish b/t Weee and AZF, which both utilize requests
# all functions inherit domain()
# set a keyword 'weee' as an input to call polymorph on the non-HTMLSession variant

def get_data(url):
    tag = '' #initialize as empty string
    d = domain(url)
    #switch statement for domain of URL --> different keyword (store in constants.py)
    #ralphs
    if d == c.grocer[0]: 
        print("ralphs") #visualize
        s = HTMLSession() #for some reason cannot use requests for ralphs
        r = s.get(url)
        ralph = bp(r.text, 'html.parser')
        tag = ralph.find("data", class_= "kds-Price kds-Price--alternate mb-8")
        if tag != None:
            tag = tag.get("value") # tag may change based on a strikethrough indicating discount
        #tag = doc.data.get("value")  #also returns same value
        #print(tag) #debug
    #weee
    elif d == c.grocer[1]:
        print("weee")
        w = requests.get(url, headers= c.cred)
        weee = bp(w.content, 'lxml')
        tag = weee.find("div", class_= "Header_price_price__4mkmc") # tag may change based on a strikethrough indicating discount
        if tag != None and tag.find("$") != -1: #check type before calling str function
            tag = tag.get_text() 
            j = tag.find("$")
            tag = tag[j+1:] #omit $ sign
        #print(tag)
    #amazonfresh
    elif d == c.grocer[2]:
        print("azf")
        a = requests.get(url, headers= c.cred)
        azf = bp(a.content, 'lxml')
        tag = azf.find('span', attrs={"id":'priceblock_ourprice'})
        if tag != None and tag.find("$") != -1: #check type before calling str function
            tag = tag.get_text() 
            j = tag.find("$")
            tag = tag[j+1:] #omit $ sign
    if tag == None or tag == '':
        if c.attempt == 1:
            return "NaN" #keyword to not modify the entry in sheet df
        # occasionally normal runs return unavailble, so double check.
        c.attempt = c.attempt + 1
        print(c.attempt)
        get_data(url) # try again
    else:
        return tag # can be none nonetype

def domain(url):
    for n in c.grocer:
        d = url.find(n, 12) # ignore "https://www."
        if d == 12:
            return n
    # now we know our domain from the url