from flask import Flask
from flask import request
from flask import jsonify 

import requests
import logging
import os
import sys
from datetime import datetime, time


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)

def get_part_of_day(h):
    return (
        "Bom dia!"
        if 5 <= h <= 17
        else "Boa tarde"
        if 18 <= h <= 22
        else "Boa noite"
    )

@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    """__summary__: Get message from the webhook"""
    vt = os.environ.get("VERIFY_TOKEN", default="true")
    wpp = os.environ.get("WPP_TOKEN", default="")

    if request.method == "GET":
        if request.args.get('hub.verify_token') == vt:
            return request.args.get('hub.challenge')
        return "Authentication failed. Invalid Token."
    messages = request.get_json()['entry'][0]['changes'][0]['value']['messages']
#    client = WhatsAppWrapper()
#    response = client.process_webhook_notification(request.get_json())
    my_headers = {'Authorization' : 'Bearer ' + wpp, 'Content-Type': 'application/json'}
    my_mes = { 'messaging_product': 'whatsapp', 'to': '5567991910048', "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }
    ola = { 'messaging_product': 'whatsapp', 'to': '', 'type': 'template', 'template': { 'name': 'saudacao', 'language': { 'code': 'en_US' }, 'components': [{'type' : 'body', 'parameters' : [{'type': 'text', ''}]}] } }
    host = 'https://graph.facebook.com/v17.0/105496645940349/messages'

    list_of_saudacoes = ['oi','ola', 'eae', 'eai',  'bom dia']
    part = get_part_of_day(datetime.now().hour)
    print(datetime.now())

    if now_time >= time(23,00) or now_time <= time(8,00):
    if messages[0]:
       message = messages[0]['text']['body'] 
       if any(substring in message.lower() for substring in list_of_saudacoes):
          requests.post(host, headers=my_headers, json=) 
       if 'modulo' in messages[0]['text']['body']: 
          response = requests.post('https://graph.facebook.com/v17.0/105496645940349/messages', headers=my_headers, json=my_mes)
          #print(response.content)

    # Do anything with the response
    # Sending a message to a phone number to confirm the webhook is working

    return jsonify({"status": "success"}, 200)

@app.route('/about')
def about():
    return 'About'
