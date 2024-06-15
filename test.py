import requests
import random
import json
import string

#Base URL:
from requests import head
base_url = "https://gorest.co.in"

#Auth Token:
auth_token = "Bearer 37ec06a4cdea57e75a398ef2d81e658897b04fb384a086e51e28bf9ac57fd365"

#get random email id:
def generate_random_email_name():
    domain = "automation.com"
    email_length = 10
    random_string = "".join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email = random_string+"@"+domain
    return email

#GET Request:
def get_request():
    url = base_url + "/public/v2/users/"
    print("GET url:", url)
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers = headers)
    assert response.status_code == 200
    json_data  = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print("........GET USER IS DONE.........")
    print(".......=================..................")

#POST REUEST:
def post_request():
    url = base_url + "/public/v2/users/"
    print("POST url:", url)
    headers = {"Authorization" : auth_token}
    data = {
    "name": "Saranraj1",
    "email": generate_random_email_name(),
    "gender": "male",
    "status": "active"
    }
    response = requests.post(url, json=data, headers = headers)
    json_data  = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body :", json_str)
    user_id = json_data["id"]
    print("user_id :", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Saranraj1"
    return user_id
    print("...........POST/CREATE USER IS DONE..................")
    print(".........===================...................")

#PUT Request:
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url:", url)
    headers = {"Authorization" : auth_token}
    data = {
    "name": "Saranraj1",
    "email": generate_random_email_name(),
    "gender": "male",
    "status": "active"
    }
    response = requests.put(url,json=data,headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("json PUT response body",json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Saranraj1"
    print("...........PUT USER IS DONE..................")
    print(".........===================...................")

#DELETE Request:
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url:", url)
    headers = {"Authorization" : auth_token}
    response = requests.delete(url,headers=headers)
    assert response.status_code == 204
    print("...........DELETE USER IS DONE..................")
    print(".........===================...................")

get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
