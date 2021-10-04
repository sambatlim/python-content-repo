import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['API_KEY']
acc_sid = os.environ['ACC_SID']
auth_token = os.environ['AUTH_TOKEN']

params = {
    'lat': 13.629065,
    'lon': 79.424446,
    'appid': api_key,
    'exclude': 'current,daily,minutely'
}
res = requests.get('xxxxxxx', params=params)
res.raise_for_status()
data = res.json()
data_len = int(len(data['hourly']) / 4)
will_rain = False

for i in range(data_len - 1):
    temp_id = data['hourly'][i]['weather'][0]['id']
    if int(temp_id) < 700:
        will_rain = True

if will_rain:
    client = Client(acc_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, don't be so moody 👊🏼",
        from_='+YOURNUMBER',
        to='+YOURNUMBER'
    )
    print(message.status)
