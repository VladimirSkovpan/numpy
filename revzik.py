import requests
import json
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()

api_key = 'OY62azZFNJ1rJgeMy7G9DbPPiFiSADveqDSM7am4'

def fetchAsteroidNeowsFeed():
  URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed?"
  params = {
      'api_key':api_key,
      'start_date':'2020-08-22',
      'end_date':'2020-08-29'
  }
  response = requests.get(URL_NeoFeed,params=params).json()
  for dates in response["near_earth_objects"]:
      pp.pprint(response["near_earth_objects"][dates][0]["name"])
fetchAsteroidNeowsFeed()