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
                "Total Deaths: " + "{:,}".format(deaths) + "\n"\
                "Total Recoveries: " + "{:,}".format(recovered) + "\n"\
                "New Confirmed Cases: " + "{:,}".format(new_confirmed) + "\n"\
                "Deaths Today: " + "{:,}".format(new_deaths) + "\n"\
                "Recoveries Today: " + "{:,}".format(new_recovered))


    #request to api.covid19api.com
    LAST_SEEN = "last_seen.txt"
    PREV_CONFIRMED = "previous_confirmed.txt"

    #request = requests.get('https://api.covid19api.com/summary', timeout=2.50)
    #parsed = json.loads(request.content.decode('UTF-8'))

    url = 'https://api.covid19api.com/summary'
    r = requests.get(url)

    if 'json' in r.headers.get('Content-Type'):
        parsed = r.json()
    else:
        print('Response content is not in JSON format.')
        js = 'spam'

    date = parsed['Countries'][177]['Date']
    date = str(date).split('T', 1)[0]

    if read_last_seen(LAST_SEEN) != date:
        store_last_seen(LAST_SEEN, date)
        print(read_last_seen(LAST_SEEN) + " has been added to last_seen.txt")
        confirmed = parsed['Countries'][177]['TotalConfirmed']
        deaths = parsed['Countries'][177]['TotalDeaths']
        new_confirmed = parsed['Countries'][177]['NewConfirmed']
        new_deaths = parsed['Countries'][177]['NewDeaths']
        new_recovered = parsed['Countries'][177]['NewRecovered']
        recovered = parsed['Countries'][177]['TotalRecovered']

        post = Post(confirmed, deaths, recovered, new_confirmed, new_deaths, new_recovered)
        #twitter api request
        #api.update_status(post.postFormat())
        print(post.postFormat())

    #time.sleep(86400)