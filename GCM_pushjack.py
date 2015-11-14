
from pushjack import GCMClient

#client = GCMClient(api_key='AIzaSyBdDg8GcXcButC78VqRDfI58zspbnGb6QY')
client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E') #new 
#registration_id = ['APA91bEktvHk0jSRf8Yj8KU9el5H4N03LaIVq6y2blvPw1NzFErkb71kOBFtmbjBr2H9hzbpP9WB1EEyO_DxIdlgMfuc0ZVXem47mKHJ72JopJutV_Tjr34S3b8iRO5l6IPhX9fn6rN4', 'APA91bHUFID4VeUT32MRzg1lGwfjtxkEIaPZKTxqRfdW7gXOJTFA3hzR7lUh8EzC-FpGEiC207Vn_Inw06nLvGQoxlL7shitn-YoYzkpXGr8GhYzxdpWf9SFJwBeRLq6Ym947_q34Hz6', 'APA91bEr_pQ9kmiq1Yd8LuK9mj732lTn0fAiSwntwrO9DXu5BzWG8JrkfE_LR9otC7fVlbFnPWS4Ztef7Hc-8v2crPNGEW5Ky1SFgxAnpQ-QLY6iR5Z33liMneLgOffgjrLLd6LPEoIU']
registration_id = ['e3Lg_f0BMTw:APA91bH_WAuDPGCL37xG9EPN1IfRTzwLYf9j4QrYd-nZG1oKKJ0gUglf2pL_Wz3hMuJf97aOVwdNYLo98cMZpNbbApKkQmYeYIQORPGJUDFMGs0M5Z1lmvylvyfI_WHw0Zr4LRg47R3a', 'eE3Sfrw0Gag:APA91bEELVL6YiLly1RW3O3LPXcIlKy_1Zu6xKmj3A8dXKw5UxoSccecowKVDCcdmK8FHeWkKDBCnYaXMXfrKHan9NUfbdDI3Js5nYj2sDE81Kd0t905fyS9NOJo1ONxn69-72Z9Rkgf']
#registration_id = ['eQDb0uPsgMA:APA91bGGtTcqe6UCWPwifM96l2Pmc1R7boEemjRSzzJkYYQdGOr_j93ZZAn4Li-jKqKqiai6wTAhoS9JFKcezBMCeV8tjwLUzIJkIdbi6BMDUwGvKtTF3wpwAKDDjbxwlQxXrxYhpxTi', 'cHaMQxCT0IY:APA91bHJ0x7CxgGf-pYnpPrLGgG3x4Se5o04_wzl8RM8L1BqCWJ7onvQKIMgZHnZ610-oQ9V-MMNIY4atUm-cWNfIFLCwdEV8xyWnVjyzLo8NBHJ_S7MIubd5rycbriUozvfLxAIauVs']
#registration_id = ['APA91bGr1ox-Tas3Fl5L3yubamiLvdh05WJIlXPJIZKcZQLTjOeBV1PDIXYUzObIiJhrZ0w6ytTbUh8CtESMXfcjQ2RArZf--YLrDuPydKSPherI9_HpUq4Q5fgbdiBk73o1PwGzCe2a']
#notifincation_id = 1 numeric for every notification
#show_ind = 0,1,2 - 2 for image notification
#data_update = 0,1
#message = 'text' or empty
#time = timestamp
#dish_photo
#user_photo
#banner = for pic to be displayed on notification
alert = 'Hello world.'
data = {'the_message' : '230@_@1@_@0@_@Thanks for being part of Ketchupp!!@_@03/08/2015 15:00:06@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'}
#notification_id - unique for every notification and ever increasing
# 11 for data update
# 1, 0 - if 0 then no update and if 1 then update
# string - location - for future use
#data = {'the_message' : '160@_@11@_@1@_@location'}
# Send to single device.#http://www.medicalweightcenter.com/files/318.jpg
# Keyword arguments are optional.
res = client.send(registration_id,
                  data,
                  collapse_key='collapse_key',
                  delay_while_idle=False,
                  time_to_live=604800)

# List of requests.Response objects from GCM Server.
res.responses
# List of messages sent.
res.messages
# List of registration ids sent.
res.registration_ids
# List of server response data from GCM.
for item in res.data:
	print item
print res.data
# List of successful registration ids.
res.successes
# List of failed registration ids.
res.failures
# List of exceptions.
res.errors
# List of canonical ids (registration ids that have changed).
res.canonical_ids
print res.canonical_ids

# Send to multiple devices by passing a list of ids.
#client.send([registration_id], alert, **options)
#client.send(registration_id,
#                  data,
#                  collapse_key='collapse_key',
#                  delay_while_idle=True,
#                  time_to_live=604800)