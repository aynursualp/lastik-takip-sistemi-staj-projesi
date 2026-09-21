import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def sms_gonder(alici_numara, metin):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_numara = os.getenv('TWILIO_PHONE_NUMBER')

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = metin,
            from_= twilio_numara,
            to = alici_numara
        )
        print(f"SMS başarıyla gönderildi! İşlem ID: {message.sid}")
        return True
    except Exception as e:
        print(f"SMS gönderme hatası: {e}")
        return False