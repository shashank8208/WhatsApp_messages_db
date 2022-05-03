# Create your views here.

from urllib import response
from django.shortcuts import render
from pickle import FALSE
import requests
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . models import WhatsApp_message

url1 = "https://13.233.94.160:9090"

################# To get the auth token##########################

def get_token():
    url = url1+"v1/users/login"
    payload = json.dumps({
  "new_password": "Khairnar@123"
})
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic '
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    rs = response.text
    json_data = json.loads(str(rs))
    response.close()
    return json_data["users"][0]["token"]


@csrf_exempt
def message(request):
    if request.method == 'POST':
        print(request.body)
        body = json.loads(request.body)
        if "messages" in body: 
            wa_id = body["messages"][0]["from"]
            msg_id = body["messages"][0]["id"]
            msg = body["messages"][0]["text"]["body"]
            timestamp = body["messages"][0]["timestamp"]
            msg_type = body["messages"][0]["type"]
            try:
                print("Saving in DB")
                # msgs = WhatsApp_message(
                #     phone_number = wa_id,
                #     type = msg_type,
                #     message = msg,
                #     msg_id = msg_id,
                #     timestamp = timestamp
                # )
                msgs = WhatsApp_message()
                msgs.phone_number = wa_id
                msgs.type = msg_type
                msgs.message = msg
                msgs.msg_id = msg_id
                msgs.timestamp = timestamp
                msgs.save()
            except Exception as e:
                print(e)
        return HttpResponse("YOYO THIS IS POST ",status=200)
        
    elif request.method == 'GET':
        print("YOYO THIS IS GET")
        return HttpResponse("YOYO THIS IS GET ",status=200)


