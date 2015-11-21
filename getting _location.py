from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
import requests
from pushjack import GCMClient
import json

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
#GCM_Client
client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E')
registration_id=['c1vU878e5Kc:APA91bGY4CEH00EUlgjuJcIHeMRmP8x6Bye6PNgBsTQ1SE_OnA05owpgj--8ukoYf5x5fa3AssZwuVYzS0eIQ-DUzGxZmUVr1hm125jhoZh4CZUqA41jV0Ji8mZMFql5g2hjTza2SLE8']
data = {'the_message' : '231@_@2@_@0@_@Thanks for being part of Ketchupp!!@_@03/08/2015 15:00:06@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'}


#function to send notification to my mobile....
def send_note(res):
	client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E')
	registration_id=['c1vU878e5Kc:APA91bGY4CEH00EUlgjuJcIHeMRmP8x6Bye6PNgBsTQ1SE_OnA05owpgj--8ukoYf5x5fa3AssZwuVYzS0eIQ-DUzGxZmUVr1hm125jhoZh4CZUqA41jV0Ji8mZMFql5g2hjTza2SLE8']
	data = {'the_message' : '267@_@1@_@0@_@'+ str(res) +'@_@03/08/2015 15:00:06@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'}
	res_ = client.send(registration_id,
                  data,
                  collapse_key='collapse_key',
                  delay_while_idle=False,
                  time_to_live=604800)


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
			# print args['lat'
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
			to_send='Locality-1:'+l1+' locality-2:'+l2+' locality-3:'+l3+'user id='+args['user_id']
			data = {'the_message' : '246@_@1@_@0@_@'+str(to_send)+
			'\@_@03/08/2015 15:00:06@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg\
			@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'}
			res = client.send(registration_id,
                  data,
                  collapse_key='collapse_key',
                  delay_while_idle=False,
                  time_to_live=604800)
			return jsonify({"result":result})
					
			# result={"lat":args['lat'],"long":args['long']}
			# return jsonify({"result":result})

class friends_list(restful.Resource):
	def post(self):
		args=parse.parse_args()
		result={}
		if args['ketchupp_id']!= None:
			client = MongoClient()
			conn = MongoClient('ds045694.mongolab.com', 45694)
			db = conn["testk"]
			db.authenticate("ketchuppuser", "ketchupp")
			_id=args['ketchupp_id']
			rows=db.users_tbl.find({"user_friends":{ "$ne" : ""},"ketchupp_id":_id},{"user_friends":1,"_id":0})
			for row in rows:
				row_json=json.loads(row.get("user_friends"))
				for rr in row_json:
					result[rr['name']]=rr['id']


			send_note(result)
			result=jsonify({"result":result})
			# send_note(result)
			return result


api.add_resource(my_api,'/first')
api.add_resource(get_api,'/first/second')
api.add_resource(get_location,'/locate')
api.add_resource(friends_list,'/friends')

parse=reqparse.RequestParser(bundle_errors=True)
parse.add_argument('city',type=str,required=False,location=['form','headers','args'])
parse.add_argument('dish_name',type=str,required=False,location=['form','headers','args'])
parse.add_argument('lat',type=str,required=False,location='form')
parse.add_argument('long',type=str,required=False,location='form')
parse.add_argument('user_id',type=str,required=False,location='form')
parse.add_argument('ketchupp_id',type=str,required=True,location='form')




if __name__ == '__main__':
	app.run(debug=True)

# 28.562126,%2077.281526
# 28.362538, 79.419897
#28.469219, 77.067737