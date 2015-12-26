
import requests
from bs4 import BeautifulSoup


#Crawler



info='http://simpleindianrecipes.com/nonveggravies.aspx'
dat=requests.get(info)
data=dat.text
soup=BeautifulSoup(data)
for link in soup.findAll('td',{'style':'text-align: center; vertical-align: top;'}):
	# title=line.string
	addr=link.findAll('img')
	print addr[0].get('src')
	# print link


chickencurryS.JPG
spicyfishcurryS.JPG
eggcurryS.JPG
butterturkeyS.JPG
fishcurryS.JPG
turkeykurmaS.JPG
Chicken fry masala S.JPG
chickentikkamasalaS.JPG
pepperchickenmasalaS.JPG
shrimpcurryS.JPG
cranberryfishS.JPG
sesamechickenS.JPG
almondchickenS.JPG
fishmoleeS.JPG
shahimuttonS.jpg
curdchickenS.jpg
chicken%20vindaloo%20S.jpg
green%20chicken%20curry%20S.JPG
kozhi%20rasam%20S.jpg
seafood%20medley%20curry%20S.jpg
methi%20chicken%20S.jpg
egg%20kurma%20S.jpg
spicy%20chicken%20curry%20S.jpg
rab%20kurma%20S.jpg
/portals/0/sirimages/karuvaatu%20kulambu%20S.jpg
/portals/0/sirimages/kheema%20kofta%20curry%20S.jpg
/portals/0/sirimages/fish%20mappas%20S.png
/portals/0/sirimages/beef%20stew%20S.jpg
/portals/0/sirimages/crabcurryS.jpg
/portals/0/sirimages/food_4.gif
/portals/0/sirimages/food_4.gif
food_4.gif
Mutton Curry S.jpg
Country Eggs S.jpg
food_4.gif
Achari_Murg_S.jpg
Naadan-Chicken-Curry-S.jpg
Malabar-Chicken-Curry-S.jpg
Prawns-JackFruit-Seeds-Curry-S.jpg
Egg-Masala-S.jpg