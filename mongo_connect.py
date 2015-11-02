from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse


application=Flask('__name__')
api=restful.Api(application)

client = MongoClient()
conn = MongoClient('ds045694.mongolab.com', 45694)
db = conn["testk"]
# MongoLab has user authentication
db.authenticate("ketchuppuser", "ketchupp")
rows=db.testk_tbl1.find({})
# for row in rows:
# 	print row['name']

class testapi(restful.Resource):
	def post(self):
		args = name_parser.parse_args() 
		rows = db.testk_tbl1.find({'name' : args['name']},{'_id' : 0})
		result = [row for row in rows]
		print result
		#for row in rows:
		#	print row
		return jsonify({'result' : result})
api.add_resource(testapi,'/testapi')
name_parser = reqparse.RequestParser()
name_parser.add_argument('name',type = str, required = False, location = 'form')

if __name__== '__main__':
	application.run(debug=True)