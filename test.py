from flask import Flask
from flask import request
from flask import render_template,url_for
import datetime
from pushjack import GCMClient
import json

app=Flask(__name__)



@app.route('/form_flask')
def show_form():
	return render_template('form.html')

@app.route('/data_form',methods=['POST','GET'])
def send_notification():
	if request.method=='POST':
		not_id=request.form['not_id']
		mess_type=request.form['mess_type']
		mess_body=request.form['mess']
		mess_head=request.form['mess_head']
		option1=request.form['op1']
		option2=request.form['op2']
		option3=request.form['op3']
		op3bool=request.form['bool']
		banner_url=request.form['banner_url']
		send_type=request.form['send_type']

		format_date='%Y-%m-%d %I:%M %p'
		now = datetime.datetime.now().strftime(format_date)

		if op3bool=="1":
			mess_bool=True
		elif op3bool=="0":
			mess_bool=False

		message_str=not_id+"@_@"+mess_type+"@_@0@_@"+mess_body+"@_@"+now+"@_@"+str(mess_bool)+"@_@"
		message_str=message_str+"https://s3-us-west-2.amazonaws.com/imagesketchupp/ketchupp_icon.png"+"@_@"+banner_url
		message_str=message_str+"@_@"+mess_head+"@_@"+option1+"@_@"+option2+"@_@"+option3

		message= {'the_message' : '2351@_@2@_@0@_@Thanks for being part of Ketchupp!!@_@03/08/2015 15:00:06@_@\
						https://s3-us-west-2.amazonaws.com/imagesketchupp/profile_pic1.png@_@https://s3-us-west-2.amazonaws.com/imagesketchupp/25a.jpg@_@http://www.fun54.com/wp-content/uploads/2011/08/beautiful-multi-colours-tortoise-wearing-a-blue-cap-saving-himself-with-rain-hd-wallpapers-1920-x-1200.jpg'}

		# data={'the_message':str(message_str)}
	
		client = GCMClient(api_key = 'AIzaSyAhjC4roIPtvL9cwcSjjqlEVfgi94qvp0E')
		registration_id=['eA1osdrEM8Y:APA91bGONONBO3AOUNZ2jGj-WYMP-QQlTtEv_BhM44i8XJQMCWd3-xQ56B53XyM-UQdUmVbzx7a8MP_0BMFhgHkG8B256Rfgjh-balgf71akBRkabmGxA4ZAucKf3gEQCmWmpBve1aQn']

		res = client.send(registration_id,
                  message,
                  collapse_key='collapse_key',
         
                delay_while_idle=False,time_to_live=604800)

		print "--------------------response---------------"
        print res.errors
        print res.successes
        print res.failures
        print res.registration_ids
        print res.responses
        print res.data
        print "--------------------------------------------"
        return json.dumps({"error": ':::'.join(res.errors), "success":':::'.join(res.successes)})
		


	return "error"


if (__name__)=='__main__':
	app.run(debug=True)
	# app.run(debug=True,host='192.168.0.10')
