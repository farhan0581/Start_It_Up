from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse

#flask application object
application=Flask('__name__')

api=restful.Api(application) #the main entry point of the application

client = MongoClient()

conn = MongoClient('ds045694.mongolab.com', 45694)

db = conn["testk"]
# MongoLab has user authentication
db.authenticate("ketchuppuser", "ketchupp")
rows=db.testk_tbl1.find({})
# for row in rows:
# 	print row['name']

class testapi(restful.Resource):   #restful.Resource represents the abstract class
	def post(self):
		args = name_parser.parse_args() 
		rows = db.testk_tbl1.find({'name' : args['name']},{'_id' : 0})
		result = [row for row in rows]
		print result
		#for row in rows:
		#	print row
		return jsonify({'result' : result})

#add resource to the api ,argument is name of the class and
#the urls,and can also define the endpoints
api.add_resource(testapi,'/testapi') 
name_parser = reqparse.RequestParser()
name_parser.add_argument('name',type = str, required = False, location = 'form')

if __name__== '__main__':
	application.run(debug=True)

