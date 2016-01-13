# import requests

# url = 'http://sing-ketchupp-v1.elasticbeanstalk.com/byspecificrestaurant'
# param = {
#         'rest_id':'1012001',
#         'dish_id':'101200111',
#         'ketchupp_id':'0'
# }
# res = requests.post(url,data = {"rest_id":"1012001","dish_id":"101200111","ketchupp_id":"0"})
# res = res.json()
# arr=res["restaurants"]["dish_details"][0]
# print arr["dish_id"]
# # abdkhalid9987@gmail.com
# # imakmob_aws
# #ec2-52-10-198-34.us-west-2.compute.amazonaws.com
from pushjack import GCMClient

message= {'the_message' : '2351@_@2@_@0@_@Thanks for being part of Ketchupp!!@_@03/08/2015 15:00:06@_@\
						https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'}

		# data={'the_message':str(message_str)}
	
client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E')
registration_id=['eA1osdrEM8Y:APA91bGONONBO3AOUNZ2jGj-WYMP-QQlTtEv_BhM44i8XJQMCWd3-xQ56B53XyM-UQdUmVbzx7a8MP_0BMFhgHkG8B256Rfgjh-balgf71akBRkabmGxA4ZAucKf3gEQCmWmpBve1aQn']

res = client.send(registration_id,
                  message,
                  collapse_key='collapse_key',
                  delay_while_idle=False,time_to_live=604800)
