from flask import Flask
from flask import request
import logging
import os

app = Flask(__name__)


@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    """__summary__: Get message from the webhook"""
    vt = os.environ.get("VERIFY_TOKEN", default="true")

    if request.method == "GET":
        if request.args.get('hub.verify_token') == vt:
            return request.args.get('hub.challenge')
        return "Authentication failed. Invalid Token."

    client = WhatsAppWrapper()
    logging.warning(str(request.get_json()))

    response = client.process_webhook_notification(request.get_json())

    # Do anything with the response
    # Sending a message to a phone number to confirm the webhook is working

    return jsonify({"status": "success"}, 200)

@app.route('/about')
def about():
    return 'About'
