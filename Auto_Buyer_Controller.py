from bs4 import BeautifulSoup
from helium._impl import ClickableText
import Auto_Buyer
from Auto_Buyer import playerPrice
from Auto_Buyer import playerName
from helium import *
from selenium import *
import time
#print (playerPrice)



username = 'labereof@bk.ru'
password = 'Ww123456'
url = 'https://www.ea.com/fifa/ultimate-team/web-app/'
browser = start_chrome(url, headless=False)

#EQUATION STATION#
playerPrice = playerPrice.replace(',', '') 
intPlayerPrice = int(playerPrice)
tax = intPlayerPrice * .05
priceAfterTax = intPlayerPrice - tax
print(priceAfterTax)
profitPerCard = 100
buyFor = priceAfterTax - profitPerCard
buyFor = int(buyFor)
print(buyFor)
#EQUATION STATION#



click(Text('Login'))
write(username, into='Enter your phone or email')
write(password, into='Enter your password')
click(Text('Sign in'))
input("Press ENTER after filling CAPTCHA")
click(Text('Transfers'))
click(Text('Search'))
write(playerName, into= 'Type Player Name')
click(Text(playerName))
#add line here to make it click on the right name.

input("Press ENTER after filling CAPTCHA")

press(TAB)
press(TAB)
press(TAB)
write(buyFor)
click(Button('Search'))


input("Press ENTER after filling CAPTCHA")
click('Make Bid')
time.sleep(3)
click(S("//html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[2]"))
time.sleep(3)
click('Make Bid')

#playerOne = class="listFUTItem has-auction-data selected"


#playerOne = Text('Dier', below=Text('SEARCH RESULTS'))
#playerTwo = Text('Dier', below=playerOne)
#click(playerTwo)

#loop that starts by clicking dier bellow Search Rsults. Loop then makes Dier = dier below dier then increase count by one until 20 (number per page)



input("Press ENTER after filling CAPTCHA")


#ClickableText.S("//html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input")
#write(buyFor, into=helium.S("//html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input"))

#use helium.press(key) to press a key 
#elem.click to click something
#webapp link https://www.ea.com/fifa/ultimate-team/web-app/