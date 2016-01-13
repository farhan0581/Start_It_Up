import requests

url = 'http://sing-ketchupp-v1.elasticbeanstalk.com/byspecificrestaurant'
param = {
        'rest_id':'1012001',
        'dish_id':'101200111',
        'ketchupp_id':'0'
}
res = requests.post(url,data = {"rest_id":"1012001","dish_id":"101200111","ketchupp_id":"0"})
res = res.json()
arr=res["restaurants"]["dish_details"][0]
print arr["dish_id"]
# abdkhalid9987@gmail.com
# imakmob_aws
#ec2-52-10-198-34.us-west-2.compute.amazonaws.com

