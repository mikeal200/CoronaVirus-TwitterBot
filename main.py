import requests
import json
from oauth import api
import tweepy
from read_write import read_last_seen, store_last_seen

#request to corona-api
FILE_NAME = "last_seen.txt"

request = requests.get('http://corona-api.com/countries/US', timeout=2.50)
parsed = json.loads(request.content.decode('UTF-8'))
date = parsed['data']['timeline'][0]['date']
print(date)

if read_last_seen(FILE_NAME) != date:
    store_last_seen(FILE_NAME, date)
    print(read_last_seen(FILE_NAME) + " has been added to last_seen.txt")

#twitter api request
api.update_status("sup")