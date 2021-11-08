from helium import *
from bs4 import BeautifulSoup

url = 'https://www.futbin.com/22/player/371/messi'
browser = start_chrome(url, headless=False)

html = browser.page_source

#print(html)

soup = BeautifulSoup(browser.page_source, "html.parser")
#print (soup)
results = soup.find_all("div", {"class": "bin_price lbin"})
#print(results)
lowestOne = soup.find(id= "xbox-lowest-1")
playerPrice = str(lowestOne.text)
print(playerPrice)
