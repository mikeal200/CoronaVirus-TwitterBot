import requests
import json
import time
from oauth import api
from read_write import read_last_seen, store_last_seen

while True:
    class Post:
        def __init__(self, population, active, confirmed, deaths, recovered, new_confirmed, new_deaths, new_recovered):
            self.population = population    
            self.active = active
            self.confirmed = confirmed
            self.deaths = deaths
            self.recovered = recovered
            self.new_confirmed = new_confirmed
            self.new_deaths = new_deaths
            self.new_recovered = new_recovered

        def postFormat(self):
            return format("US Covid-19 Daily Statistics\n\n"\
                "Population: " + "{:,}".format(population) + "\n"\
                "Active Cases: " + "{:,}".format(active) + "\n"\
                "Confirmed Cases: " + "{:,}".format(confirmed) + "\n"\
                "Total Deaths: " + "{:,}".format(active) + "\n"\
                "Total Recoveries: " + "{:,}".format(recovered) + "\n"\
                "New Confirmed Cases: " + "{:,}".format(new_confirmed) + "\n"\
                "Deaths Today: " + "{:,}".format(new_deaths) + "\n"\
                "Recoveries Today: " + "{:,}".format(new_recovered))


    #request to corona-api
    FILE_NAME = "last_seen.txt"

    request = requests.get('http://corona-api.com/countries/US', timeout=2.50)
    parsed = json.loads(request.content.decode('UTF-8'))

    date = parsed['data']['timeline'][0]['date']

    if read_last_seen(FILE_NAME) != date:
        store_last_seen(FILE_NAME, date)
        print(read_last_seen(FILE_NAME) + " has been added to last_seen.txt")
        population = parsed['data']['population']
        active = parsed['data']['timeline'][0]['active']
        confirmed = parsed['data']['timeline'][0]['confirmed']
        deaths = parsed['data']['timeline'][0]['deaths']
        new_confirmed = parsed['data']['timeline'][0]['new_confirmed']
        new_deaths = parsed['data']['timeline'][0]['new_deaths']
        new_recovered = parsed['data']['timeline'][0]['new_recovered']
        recovered = parsed['data']['timeline'][0]['recovered']
        post = Post(population, active, confirmed, deaths, recovered, new_confirmed, new_deaths, new_recovered)
        #twitter api request
        api.update_status(post.postFormat())

    time.sleep(1200)