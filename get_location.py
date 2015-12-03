from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
import requests
from pushjack import GCMClient
import json


app=Flask(__name__)
api=restful.Api(app)


#class to get loaclity 1,2,3 from google map api,accepts latitude as lat,longitude as long as parameter
class get_location(restful.Resource):
	def post(self):
		args=parse.parse_args()
		if args['lat'] !=None and args['long'] !=None:
			info='https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(args['lat'])+", "+str(args['long'])+'&key=AIzaSyCD81KWvRb-3Vv38BVouOTwCWgwi3Lfl9Y'
			dat=requests.get(info)
			data=dat.json()
			#default result
			l1='Not Found'
			l2='Not Found'
			l3='Not Found'
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
					
		else:
			result="enter the details"
			return jsonify({"result":result})




api.add_resource(get_location,'/locate')

parse=reqparse.RequestParser(bundle_errors=True)
parse.add_argument('lat',type=str,required=True,location='form')
parse.add_argument('long',type=str,required=True,location='form')
# parse.add_argument('user_id',type=str,required=True,location='form')


if __name__ == '__main__':
	app.run(debug=True)
