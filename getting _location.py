from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
import requests

# info='https://maps.googleapis.com/maps/api/geocode/json?latlng=28.562126,%2077.281526&location_type=GEOMETRIC_CENTER&key=AIzaSyCD81KWvRb-3Vv38BVouOTwCWgwi3Lfl9Y'
# # info='https://maps.googleapis.com/maps/api/geocode/json?latlng=28.624182,%2077.437847&location_type=GEOMETRIC_CENTER&key=AIzaSyCD81KWvRb-3Vv38BVouOTwCWgwi3Lfl9Y'
# dat=requests.get(info)
# data=dat.json()
# # print data["results"][0]["address_components"][1]
# # print len(data["results"][0]["address_components"])
# tra=data["results"][0]["address_components"]
# for count in range(len(tra)):
# 	check=tra[count]["types"]
# 	if "sublocality_level_1" in check:
# 		print tra[count]["long_name"] 



app=Flask(__name__)
api=restful.Api(app)


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

class get_api(restful.Resource):
	def get(self):
		args=parse.parse_args()
		if args['city'] != None and args['dish_name'] != None:
			rows=db.dish_tbl.find({'city':args['city'],'dish_name':args['dish_name']},
			{'_id':0,'rest_name':0,'location':0})
		elif args['city']==None and args['dish_name'] == None:
			rows=db.dish_tbl.find({},{'_id':0,'rest_name':1,'location':1})
		elif args['city'] ==None and args['dish_name']!=None:
			rows=db.dish_tbl.find({'dish_name':args['dish_name']},{'_id':0,'rest_name':1,'location':1})

		result=[row for row in rows]
		return jsonify({"result":result})

class get_location(restful.Resource):
	def post(self):
		args=parse.parse_args()
		if args['lat'] !=None and args['long'] !=None and args['user_id'] !=None:
			info='https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(args['lat'])+", "+str(args['long'])+'&key=AIzaSyCD81KWvRb-3Vv38BVouOTwCWgwi3Lfl9Y'
			dat=requests.get(info)
			data=dat.json()
			# print '###################'
			# print args['lat']
			tra=data["results"][0]["address_components"]
			for count in range(len(tra)):
				check=tra[count]["types"]
				if "sublocality_level_1" in check:
					l1=tra[count]["long_name"]
				if "sublocality_level_2" in check:
					l2=tra[count]["long_name"]
				if "sublocality_level_3" in check:
					l3=tra[count]["long_name"]

			result={"locality_1":l1,"locality_2":l2,"locality_3":l3}
			return jsonify({"result":result})
					
			# result={"lat":args['lat'],"long":args['long']}
			# return jsonify({"result":result})


api.add_resource(my_api,'/first')
api.add_resource(get_api,'/first/second')
api.add_resource(get_location,'/locate')

parse=reqparse.RequestParser(bundle_errors=True)
parse.add_argument('city',type=str,required=False,location=['form','headers','args'])
parse.add_argument('dish_name',type=str,required=False,location=['form','headers','args'])
parse.add_argument('lat',type=str,required=False,location='form')
parse.add_argument('long',type=str,required=False,location='form')
parse.add_argument('user_id',type=str,required=False,location='form')




if __name__ == '__main__':
	app.run(debug=True)

# 28.562126,%2077.281526
# 28.362538, 79.419897
#28.469219, 77.067737