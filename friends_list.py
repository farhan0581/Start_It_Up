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
# rows=db.users_tbl.find({"user_friends":{ "$ne" : ""},"ketchupp_id":idd},{"user_friends":1,"_id":0})
ls=[]
res={}
c=0
dd=""
result=[]

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


rows=db.users_tbl.find({"ketchupp_id":idd},{"GCM_ID":1,"_id":0})
for row in rows:
	print row["GCM_ID"]