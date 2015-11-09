from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse

app=Flask(__name__)
api=restful.Api(app)

client=MongoClient()

conn = MongoClient('ds045694.mongolab.com', 45694)
db = conn["testk"]
db.authenticate("ketchuppuser", "ketchupp")

# rows=db.testk_tbl1.find({})

# for row in rows:
# 	print row

class my_api(restful.Resource):
	def post(self):
		args=parse.parse_args()
		if args['city'] != None and args['dish_name'] != None:
			rows=db.dish_tbl.find({'city':args['city'],'dish_name':args['dish_name']},
			{'_id':0,'rest_name':1,'location':1})
		elif args['city']==None and args['dish_name'] == None:
			rows=db.dish_tbl.find({},{'_id':0,'rest_name':1,'location':1})
		elif args['city'] ==None and args['dish_name']!=None:
			rows=db.dish_tbl.find({'dish_name':args['dish_name']},{'_id':0,'rest_name':1,'location':1})

		
		# rows=db.dish_tbl.find({'city':args['city'],'dish_name':args['dish_name']},
			# {'_id':0,'rest_name':1,'location':1})
		result=[row for row in rows]
		return jsonify({"result":result})		

api.add_resource(my_api,'/first')
parse=reqparse.RequestParser(bundle_errors=True)
parse.add_argument('city',type=str,required=False,location='form')
parse.add_argument('dish_name',type=str,required=False,location='form')


if __name__ == '__main__':
	app.run(debug=True)