# Create your views here.

from urllib import response
from django.shortcuts import render
from pickle import FALSE
import requests
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . models import WhatsApp_message

url1 = ""

def get_token():
    url = url1 + "/v1/users/login"
    payload = "{\n\t\"new_password\": \"\"\n}"
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
        body = json.loads(request.body)
        if "messages" in body: 
            wa_id = body["messages"][0]["from"]
            msg_id = body["messages"][0]["id"]
            msg = body["messages"][0]["text"]["body"]
            timestamp = body["messages"][0]["timestamp"]
            msg_type = body["messages"][0]["type"]
            try:
                msgs = WhatsApp_message(
                    phone = wa_id,
                    type = msg_type,
                    message = msg,
                    msg_id = msg_id,
                    timestamp = timestamp
                )
                msgs.save()
            except Exception as e:
                print(e)
    return HttpResponse(status=200)

