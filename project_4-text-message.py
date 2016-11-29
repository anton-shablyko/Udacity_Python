# My twilio number: +13178848772

from twilio.rest import TwilioRestClient

account_sid = "ACfec25322253c43ce53fe13e917df9d08"
auth_token = "888e106105837d590b43f23d43a671fb"
client = TwilioRestClient(account_sid,auth_token)

client.messages.create(
    body = 'Test Test',
    to="+12013XXXX7", #mynumber
    from_="+13178848772")#my twilio number
