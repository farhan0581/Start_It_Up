from bs4 import BeautifulSoup
import requests

url='http://dir.indiamart.com/impcat/automotive-lights.html'
data=requests.get(url)
site_text=data.text
soup=BeautifulSoup(site_text)
for span in soup.findAll('li',{'class':'listing-wdt'}):
	print span.findAll('a',{'class':'product-name'})
	print span.findAll('span',{'itemprop':'name'})
	print span.findAll('span',{'class':'cityLocation'})
	print span.findAll('span',{'itemprop':'telephone'})