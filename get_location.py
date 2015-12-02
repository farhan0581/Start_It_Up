from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
import requests
from pushjack import GCMClient
import json


app=Flask(__name__)
api=restful.Api(app)


#function to send notification to my mobile....
def send_note(res):
	client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E')
	registration_id=['c1vU878e5Kc:APA91bGY4CEH00EUlgjuJcIHeMRmP8x6Bye6PNgBsTQ1SE_OnA05owpgj--8ukoYf5x5fa3AssZwuVYzS0eIQ-DUzGxZmUVr1hm125jhoZh4CZUqA41jV0Ji8mZMFql5g2hjTza2SLE8']
	data = {'the_message' : '270@_@1@_@0@_@'+ str(res) +'@_@03/08/2015 15:00:06@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'}
	res_ = client.send(registration_id,
                  data,
                  collapse_key='collapse_key',
                  delay_while_idle=False,
                  time_to_live=604800)



#class to get loaclity 1,2,3 from google map api,accepts lat,long,user_id as parameter
class get_location(restful.Resource):
	def post(self):
		args=parse.parse_args()
		if args['lat'] !=None and args['long'] !=None and args['user_id'] !=None:
			info='https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(args['lat'])+", "+str(args['long'])+'&key=AIzaSyCD81KWvRb-3Vv38BVouOTwCWgwi3Lfl9Y'
			dat=requests.get(info)
			data=dat.json()
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
			# to_send='Locality-1:'+l1+' locality-2:'+l2+' locality-3:'+l3+'user id='+args['user_id']
			return jsonify({"result":result})
					
			# result={"lat":args['lat'],"long":args['long']}
			# return jsonify({"result":result})
		else:
			result="enter the details"
			return jsonify({"result":result})




api.add_resource(get_location,'/locate')

parse=reqparse.RequestParser(bundle_errors=True)
parse.add_argument('lat',type=str,required=True,location='form')
parse.add_argument('long',type=str,required=True,location='form')
parse.add_argument('user_id',type=str,required=True,location='form')


if __name__ == '__main__':
	app.run(debug=True)

# 28.562126,%2077.281526
# 28.362538, 79.419897
#28.469219, 77.067737