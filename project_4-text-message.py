# My twilio number: +13178848772

from twilio.rest import TwilioRestClient

account_sid = "******"
auth_token = "******"
client = TwilioRestClient(account_sid,auth_token)

client.messages.create(
    body = 'Test Test',
    to="+12013XXXX7", #mynumber
    from_="+13178848772")#my twilio number
