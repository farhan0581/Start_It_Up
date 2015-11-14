# from bs4 import BeautifulSoup
# import requests
# import csv

# url='http://dir.indiamart.com/impcat/automotive-lights.html'
# space='\t\t\t\t\t'
# data=requests.get(url)
# site_text=data.text
# soup=BeautifulSoup(site_text)

# #Using csv as text file to make it more Human readable...
# f=open('details_mart.csv','w+')

# f.write("ITEM NAME"+space+"\t\t\tCOMPANY"+space+"LOCATION"+space+"CONTACT\n")
# for span in soup.findAll('li',{'class':'listing-wdt'}):
# 	product=span.findAll('a',{'class':'product-name'})
# 	company=span.findAll('span',{'itemprop':'name'})
# 	location=span.findAll('span',{'class':'cityLocation'})
# 	number=span.findAll('span',{'itemprop':'telephone'})
# 	p1=product[0].get_text()
# 	c1=company[0].get_text()
# 	l1=location[0].get_text()
# 	n1=number[0].get_text()
# 	print p1+'\n'
# 	f.write(p1+'\t\t'+c1+'\t\t'+l1+'\t\t'+n1+'\n')
# nurl='http://dir.indiamart.com/impcatProductPagination.php'
# data=requests.get(nurl)
# print data

args={}
args['lat']=1531
args['long']=513514654
args['user_id']=0
info='https://maps.googleapis.com/maps/api/geocode/json?latlng='+args['lat']+","+args['long']+'&location_type=GEOMETRIC_CENTER&key=AIzaSyCD81KWvRb-3Vv38BVouOTwCWgwi3Lfl9Y'
print info