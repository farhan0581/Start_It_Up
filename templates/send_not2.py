from pymongo import MongoClient
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
import requests
from pushjack import GCMClient
import json

app=Flask(__name__)
api=restful.Api(app)

#function to send notification to all mobiles....
def send_note(id_list,messag):
	client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E')
	# registration_id=['c1vU878e5Kc:APA91bGY4CEH00EUlgjuJcIHeMRmP8x6Bye6PNgBsTQ1SE_OnA05owpgj--8ukoYf5x5fa3AssZwuVYzS0eIQ-DUzGxZmUVr1hm125jhoZh4CZUqA41jV0Ji8mZMFql5g2hjTza2SLE8']
	data = {'the_message' : messag}
	# for i in range(len(id_list)):
	# 	registration_id=str(id_list[i])
		# print registration_id
	res_ = client.send(id_list,
                  data,
                  collapse_key='collapse_key',
                  delay_while_idle=False,
                  time_to_live=604800)

#function to send notification to user mobile only...
def send_note_me(res,_id,messag):
	client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E')
	registration_id=_id
	message=str(messag)
	# message='285@_@1@_@0@_@'+ str(res) +'@_@03/08/2015 15:00:06@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'
	data = {'the_message' : message}
	res_ = client.send(registration_id,
                  data,
                  collapse_key='collapse_key',
                  delay_while_idle=False,
                  time_to_live=604800)





#Class which finds the GCM ids of friends...
class friends_list(restful.Resource):
	def post(self):
		args=parse.parse_args()
		result={}
		if args['ketchupp_id']!= None and args['type']!=None:
			client = MongoClient()
			conn = MongoClient('ds045694.mongolab.com', 45694)
			database="testk"
			dbuser="ketchuppuser"
			dbpassword="ketchupp"
			db = conn[database]
			db.authenticate(dbuser, dbpassword)
			gcm_id_list=["c5sXcnXtvTE:APA91bEZVRZNXyV_719yTppndc0RHzkbgo-Lvp9IRSE1ojJDumtaxFliUCg049oH7cxg5zbH1taqDCVmyJ6rEWdLvzcum3rmoPYuPYB4S4Xa1RRLsm54pqOToNftDufphN0IRpsd29SG",
							"eSWGmEgZRHM:APA91bEfE_Xe7RH6X0StNSc17AH6XwlP7fVg3Qoy4ynbu8lnSbIoiFeQaUSCLcCCT69Q7eiCHA6cjlt4EPHF9hkeHOjCbLx7iuu0VOyXTa26MrjITmy2NCpfMn8XKhrfeVHS830mvhas",
							"c1vU878e5Kc:APA91bGY4CEH00EUlgjuJcIHeMRmP8x6Bye6PNgBsTQ1SE_OnA05owpgj--8ukoYf5x5fa3AssZwuVYzS0eIQ-DUzGxZmUVr1hm125jhoZh4CZUqA41jV0Ji8mZMFql5g2hjTza2SLE8"
				
			
			            ]
			msg=args['message']

			_id=args['ketchupp_id']

			#if notification to all
			if args['type']=='all':
				rows=db.users_tbl.find({"user_friends":{ "$ne" : ""},"ketchupp_id":_id},{"user_friends":1})
				for row in rows:
					row_json=json.loads(row.get("user_friends"))
					for rr in row_json:
						gcm_id=db.users_tbl.find({"fb_id":int(rr['id'])},{"GCM_ID":1,"_id":0})
						for i in gcm_id:
							result[rr['name']]=i['GCM_ID']
							# gcm_id_list.append(i['GCM_ID'])



				send_note(gcm_id_list,msg)
				result=jsonify({"result":result})
				return result

			#if notification to self..	
			elif args['type']=='self':
				rows=db.users_tbl.find({"ketchupp_id":_id},{"GCM_ID":1,"_id":0})
				for row in rows:
					gcm_id=row["GCM_ID"]
				result="hello just for testing!!"
				
				send_note_me(result,gcm_id,msg)
				return jsonify({"result":True})


		#if ketchupp id is not given...
		else:
			result="PLease provide a ketchupp id"
			return jsonify({"result":result})


api.add_resource(friends_list,'/friends')

parse=reqparse.RequestParser(bundle_errors=True)
parse.add_argument('ketchupp_id',type=str,required=True,location='form')
parse.add_argument('type',type=str,required=True,location='form')
parse.add_argument('message',type=str,required=True,location='form')

if __name__ == '__main__':
	app.run(debug=True)

