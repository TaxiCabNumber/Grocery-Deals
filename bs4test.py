from bs4 import BeautifulSoup as bp
from requests_html import HTMLSession # workaround
#import re ### arg in .find(..., text=re.compile("value=.*"))
import requests
import constants as c
#write function in .py file that takes url as argument and returns only the 

#url = "https://www.ralphs.com/p/russet-potatoes/0003338353010?"
#url = "https://www.sayweee.com/en/product/Barilla-Spaghetti-Pasta/47727"
#url = "https://www.amazon.com/365-Everyday-Value-Organic-Capellini/dp/B074H6X463/"
url = "https://www.amazon.com/Prego-Italian-Pasta-Sauce-Flavored/dp/B009P7YHU8?"

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
#'Accept-Language': 'en-US, en;q=0.5'}

page = requests.get(url, headers= c.cred)

s = HTMLSession()
def getdata(url):
    r = s.get(url)
    #soup = bp(r.text, 'html.parser')
    soup = bp(r.content, 'lxml')
    return soup

#
#doc = getdata(url)
doc = bp(page.content, 'lxml')

tag = doc.find('span', attrs={"id":'priceblock_ourprice'}).get_text() #, class_="a-size-medium a-color-price") #.get_text() # tag may change based on a strikethrough indicating discount
#print(doc.prettify())

j = tag.find("$")
tag = tag[j+1:] #omit $ sign
#returns
#tag = doc.data.get('value')  #either works
#tag = tag.get('value')
print(tag)
print(type(tag))

#print(type(tag))

#data = str(tag)




#tdata = doc.data
#price = tdata
#print(tdata)

#########
# Tech with Tim bs4 Tutorial 1
#########
#result = requests.get(url)
#print(result.text)
#doc = bp(result.text, "html.parser")
#print(doc.prettify())


#with open("index.html", "r") as f:
#    doc = bp(f, "html.parser")
#tag = doc.title
# #tag.string = "hello" #modifies title of index
#print(tag)
#tagp = doc.find_all("p")[0]
#print(tagp.find_all("b"))
# doc.find_all["p", "div", "li"]

