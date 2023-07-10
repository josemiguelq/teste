from flask import Flask
from flask import request
from flask import jsonify

import requests
import logging
import os
import sys
import pytz
from datetime import datetime, time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)


def get_part_of_day(h):
    if 5 <= h <= 12:
        return "Bom dia! 🦁 🦁 📱📱"
    else:
        return "Boa tarde! 🦁 🦁 📱📱"

def message_oi(to_num):
    tz = pytz.timezone('America/Santiago')
    part = get_part_of_day(datetime.now(tz).hour)
    return {'messaging_product': 'whatsapp',
           'recipient_type': 'individual',
           'to': to_num,
           'type': 'text',
           'text': {'body': part}
           }

@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    vt = os.environ.get("VERIFY_TOKEN", default="true")
    wpp = os.environ.get("WPP_TOKEN", default="")

    if request.method == "GET":
        if request.args.get('hub.verify_token') == vt:
            return request.args.get('hub.challenge')
        return "Authentication failed. Invalid Token."
    response = request.get_json()
    print(response)
    messages = response['entry'][0]['changes'][0]['value']['messages']
    my_headers = {'Authorization': 'Bearer ' + wpp, 'Content-Type': 'application/json'}
    my_mes = {'messaging_product': 'whatsapp', 'to': '5567991910048', "type": "template",
              "template": {"name": "hello_world", "language": {"code": "en_US"}}}

    host = 'https://graph.facebook.com/v17.0/105496645940349/messages'

    list_of_saudacoes = ['oi', 'ola', 'olá', 'eae', 'eai', 'bom dia']

    if messages[0]:
        message = messages[0]['text']['body']
        to_num = messages[0]['from']
        to_num = to_num[:4] + '9' + to_num[4:]
        e_saudacao = any(substring in message.lower() for substring in list_of_saudacoes)
        print(e_saudacao)
        if e_saudacao:
            ola = message_oi(to_num)
            print(ola)
            requests.post(host, headers=my_headers, json=ola)
        if 'modulo' in messages[0]['text']['body']:
            response = requests.post(host, headers=my_headers, json=my_mes)
            # print(response.content)

    return jsonify({"status": "success"}, 200)


@app.route('/about')
def about():
    return 'About'
