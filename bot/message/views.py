from django.shortcuts import render
# Create your views here.
from urllib import response
from django.shortcuts import render
from cgitb import text
from http import HTTPStatus
from pickle import FALSE
import requests
import json
from datetime import date, datetime
import urllib3
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . models import WhatsApp_message

url1 = "https://13.233.94.160:9090"

#FUNCTION TO UPDATE AUTHKEY

def update_authkey():
    print("In Update Authkey")
    url = url1 + "/v1/users/login"
    payload = "{\n\t\"new_password\": \"Khairnar@123\"\n}"
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': 'Basic <base64(username:password)>',
        'Authorization': 'Basic YWRtaW46S2hhaXJuYXJAMTIz'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    rs = response.text
    #print(rs)
    json_data = json.loads(str(rs))
    response.close()
    return json_data["users"][0]["token"]


#FUNCTION TO SEND INTERACTIVE TEXT MESSAGE (BUTTON MESSAGE)
def send_message(to_num):
    print("In Send Message")
    url = "https://13.233.94.160:9090/v1/messages"

    payload = json.dumps({
    "to": to_num,
    "recipient_type": "individual",
    "type": "interactive",
    "interactive": {
        "type": "button",
        "header": {
            "type": "text",
            "text": "Dear Customer,"
        },
        "body": {
            "text": "Now, you can expand your business using WhatsApp Commerce. Enable your customers to Connect-Shop-Pay on WhatsApp."
        },
        "footer": {
            "text": "Choose an option by clicking on any button below:"
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "Button 1 Text",
                        "title": "Know More"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "Button 2 Text",
                        "title": "Interested"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "Button 3 Text",
                        "title": "Not Interested"
                    }
                }
            ]
        }
    }
})
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + update_authkey()
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response.text


# CODE TO SEND MESSAGES FROM CSV FILE 
if __name__ == "__main__":
    with open('me.csv','r',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exec: # Max Worker means at once how many request you want to send
            count=0
            for col in csv_reader:
                count+=1
                # phone = "91"+col[0][-10:]
                phone = col[0]
                var1 = [] 
                args1 = [phone] 

                exec.submit(send_message,*args1)
                print(phone)
                print(count)


@csrf_exempt
def message(request):
    # print("IN message")
    if request.method == 'POST':
        # print("IN POST")
        # print(type(request.body))
        body = json.loads(request.body)
        # print(body)
        # print(type(body))
        if "statuses" in body:
            pass
        elif "messages" in body: 
            in_main_body = ["messages"][0]
            wa_id = in_main_body["from"]
            msg_id = in_main_body["id"]
            msg = in_main_body["text"]["body"]
            timestamp = in_main_body["timestamp"]
            msg_type=in_main_body["type"]
            try:
                msgs = WhatsApp_message(
                    wa_id = wa_id,
                    msg_type = msg_type,
                    message = msg,
                    msg_id = msg_id,
                    timestamp = timestamp
                )
            except Exception as shlok:
                print(shlok)
            #Chatbot Here
            # msg_body = 

    #     print("**************************** Request ****************************")
    #     print(req["messages"][0]["text"]["body"])
    # #print(req["contacts"][0]["wa_id"])s

    #     print("**************************** Request ****************************")
        
    #     #************************** ChatBot *******************************
        
    #  send_message()
    return HttpResponse("Message/webhooks")


def test(request):
    return HttpResponse("test")
