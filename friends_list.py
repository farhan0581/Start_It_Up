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
idd="a319df48-3b8a-11e5-b9ac-02c462edaa43"
rows=db.users_tbl.find({"user_friends":{ "$ne" : ""},"ketchupp_id":idd},{"user_friends":1,"_id":0})
ls=[]
res={}
c=0
dd=""
for row in rows:
	rr=json.loads(row.get("user_friends"))
	for r in rr:
		# res[r['name']]=r['id']
		dd+=r['name']
print dd