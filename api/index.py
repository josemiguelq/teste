from flask import Flask
from flask import request
from flask import jsonify 

import requests
import logging
import os
import sys


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)


@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    """__summary__: Get message from the webhook"""
    vt = os.environ.get("VERIFY_TOKEN", default="true")
    wpp = os.environ.get("WPP_TOKEN", default="")

    if request.method == "GET":
        if request.args.get('hub.verify_token') == vt:
            return request.args.get('hub.challenge')
        return "Authentication failed. Invalid Token."
    print(str(request.get_json()))

#    client = WhatsAppWrapper()
#    response = client.process_webhook_notification(request.get_json())
    my_headers = {'Authorization' : 'Bearer ' + wpp, 'Content-Type': 'application/json'}
    my_mes = { 'messaging_product': 'whatsapp', 'to': '5567991910048', "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }
   # response = requests.post('https://graph.facebook.com/v17.0/105496645940349/messages', headers=my_headers, json=my_mes)
   # print(response.content)

    # Do anything with the response
    # Sending a message to a phone number to confirm the webhook is working

    return jsonify({"status": "success"}, 200)

@app.route('/about')
def about():
    return 'About'
