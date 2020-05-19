import requests
import json
import time
from oauth import api
from read_write import read_last_seen, store_last_seen, store_prev_confirmed, read_prev_confirmed

while True:
    class Post:
        def __init__(self, confirmed, deaths, recovered, new_confirmed, new_deaths, new_recovered):
            self.confirmed = confirmed
            self.deaths = deaths
            self.recovered = recovered
            self.new_confirmed = new_confirmed
            self.new_deaths = new_deaths
            self.new_recovered = new_recovered

        def postFormat(self):
            return format("US Covid-19 Daily Statistics\n\n"\
                "Confirmed Cases: " + "{:,}".format(confirmed) + "\n"\
                "Total Deaths: " + "{:,}".format(active) + "\n"\
                "Total Recoveries: " + "{:,}".format(recovered) + "\n"\
                "New Confirmed Cases: " + "{:,}".format(new_confirmed) + "\n"\
                "Deaths Today: " + "{:,}".format(new_deaths) + "\n"\
                "Recoveries Today: " + "{:,}".format(new_recovered))


    #request to api.covid19api.com
    LAST_SEEN = "last_seen.txt"
    PREV_CONFIRMED = "previous_confirmed.txt"

    request = requests.get('https://api.covid19api.com/summary', timeout=2.50)
    parsed = json.loads(request.content.decode('UTF-8'))

    date = parsed['Countries'][177]['Date']
    date = str(date).split('T', 1)[0]

    if read_last_seen(LAST_SEEN) != date:
        store_last_seen(LAST_SEEN, date)
        print(read_last_seen(LAST_SEEN) + " has been added to last_seen.txt")
        confirmed = parsed['Countries']['timeline'][0]['confirmed']
        deaths = parsed['data']['timeline'][0]['deaths']
        #new confirmed was giving innacurate statistics so i will save the previous days confirmed cases and it will subtracted by the current days confirmed cases
        #new_confirmed = parsed['data']['timeline'][0]['new_confirmed']
        new_deaths = parsed['data']['timeline'][0]['new_deaths']
        new_recovered = parsed['data']['timeline'][0]['new_recovered']
        recovered = parsed['data']['timeline'][0]['recovered']
        previous_confirmed = read_prev_confirmed(PREV_CONFIRMED)
        new_confirmed = 0

        post = Post(confirmed, deaths, recovered, new_confirmed, new_deaths, new_recovered)
        #twitter api request
        #api.update_status(post.postFormat())
        print(post.postFormat())

    #time.sleep(86400)