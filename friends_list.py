from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
import json

#flask application object
application=Flask('__name__')

api=restful.Api(application) #the main entry point of the application

client = MongoClient()

conn = MongoClient('ds045694.mongolab.com', 45694)

db = conn["testk"]
# MongoLab has user authentication
db.authenticate("ketchuppuser", "ketchupp")
idd="31685c8a-78d9-11e5-89ec-026674f3c46b"
# idd="a319df48-3b8a-11e5-b9ac-02c462edaa43"
# idd="56e0b4ce-5f86-11e5-962a-0a58c3a68d31"

# rows=db.users_tbl.find({"user_friends":{ "$ne" : ""},"ketchupp_id":idd},{"user_friends":1,"_id":0})
ls=[]
res={}
c=0
dd=""
result={}
gcm_id_list=[]

# rows=db.users_tbl.find({"ketchupp_id":idd},{"GCM_ID":1})



# for row in rows:
# 	print row

# for row in rows:
# 	rr=json.loads(row.get("user_friends"))
# 	for r in rr:
# 		gcm_id=db.users_tbl.find({"fb_id":int(r['id'])},{"GCM_ID":1,"_id":0})
# 		for i in gcm_id:
# 			res[r['name']]=i["GCM_ID"]
# 			result.append(i["GCM_ID"])
# 		# dd+=r['name']

# # print res
# for i in range(len(result)):
# 	print result[i]
# # for row in rows:
# # 	a=row["user_friends"]


# rows=db.users_tbl.find({"ketchupp_id":idd},{"GCM_ID":1,"_id":0})
# for row in rows:
# 	print row["GCM_ID"]

rows=db.users_tbl.find({"user_friends":{ "$ne" : ""},"ketchupp_id":idd},{"user_friends":1})
for row in rows:
	row_json=json.loads(row.get("user_friends"))
	for rr in row_json:
		gcm_id=db.users_tbl.find({"fb_id":int(rr['id'])},{"GCM_ID":1,"_id":0})
		for i in gcm_id:
			result[rr['name']]=i['GCM_ID']
			gcm_id_list.append(i['GCM_ID'])

for i in range(len(gcm_id_list)):
	print gcm_id_list[i]


# def funct(par):
# 	for i in range(len(par)):
# 		print par[i]



# test=['1','2']
# funct(test)