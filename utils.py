import os
import requests

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

def send_whatsapp_message(to, message):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"
    data = {
        "From": TWILIO_WHATSAPP_NUMBER,
        "To": to,
        "Body": message
    }
    response = requests.post(url, data=data, auth=(TWILIO_SID, TWILIO_AUTH_TOKEN))
    if response.status_code not in [200, 201]:
        print("Failed to send message:", response.text)
