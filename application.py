import json
import os
from tkinter import E
import stripe

from flask import Flask, jsonify, request

endpoint_secret = ""

application = Flask(__name__)

@application.route("/webhook")
def webhook():
    event = None
    payload = request.data
    sig_header = request.headers["STRIPE_SIGNATURE"]

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        raise e
    except stripe.error.SignatureVerificationError as e:
        raise e
    
    if event['type'] == 'checkout.session.async_payment_failed':
        session = event['data']['object']
    elif event['type'] == 'checkout.session.async_payment_succeeded':
        session = event['data']['object']
    elif event['type'] == 'checkout.session.completed':
        session = event['data']['object']
    elif event['type'] == 'checkout.session.expired':
        session = event['data']['object']
    else:
      print('Unhandled event type {}'.format(event['type']))
    
    return jsonify(success=True)

