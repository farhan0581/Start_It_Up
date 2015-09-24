from bs4 import BeautifulSoup
import requests
import csv

url='http://dir.indiamart.com/impcat/automotive-lights.html'
space='\t\t\t\t\t'
data=requests.get(url)
site_text=data.text
soup=BeautifulSoup(site_text)

#Using csv as text file to make it more Human readable...
f=open('details_mart.csv','w+')

f.write("ITEM NAME"+space+"\t\t\tCOMPANY"+space+"LOCATION"+space+"CONTACT\n")
for span in soup.findAll('li',{'class':'listing-wdt'}):
	product=span.findAll('a',{'class':'product-name'})
	company=span.findAll('span',{'itemprop':'name'})
	location=span.findAll('span',{'class':'cityLocation'})
	number=span.findAll('span',{'itemprop':'telephone'})
	p1=product[0].get_text()
	c1=company[0].get_text()
	l1=location[0].get_text()
	n1=number[0].get_text()
	f.write(p1+'\t\t'+c1+'\t\t'+l1+'\t\t'+n1+'\n')