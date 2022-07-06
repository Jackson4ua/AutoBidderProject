from helium import *
from bs4 import BeautifulSoup

url = 'https://www.futbin.com/22/player/750/eric-dier'
browser = start_chrome(url, headless=False)

html = browser.page_source

#print(html)

soup = BeautifulSoup(browser.page_source, "html.parser")
playerName = (soup.find("span", {"class": "header_name full-name"}).text)


lowestOne = soup.find(id= "xbox-lowest-1")
playerPrice = str(lowestOne.text)
print(playerName)
print(playerPrice)

