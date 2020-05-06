import requests
import json

FILE_NAME = "last_seen.txt"

request = requests.get('http://corona-api.com/countries/US', timeout=2.50)
parsed = json.loads(request.content.decode('UTF-8'))
date = parsed['data']['timeline'][0]['date']
print(date)

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_date = str(file_read.read().strip())
    file_read.close()
    return last_seen_date

def store_last_seen(FILE_NAME, last_seen_date):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_date))
    file_write.close()
    return

if read_last_seen(FILE_NAME) != date:
    store_last_seen(FILE_NAME, date)
    print(read_last_seen(FILE_NAME) + "has been added to last_seen.txt")
    