'''
Copied from https://www.twilio.com/docs/libraries/python
'''


from twilio.rest import TwilioRestClient
import os

#Credentials are stored as TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
client = TwilioRestClient()

message = client.messages.create(body="Hello from Python",
    to=os.environ['MY_PHONE_NUMBER'],    # Replace with your phone number
    from_=os.environ['TWILLIO_PHONE_NUMBER']) # Replace with your Twilio number

print(message.sid)
