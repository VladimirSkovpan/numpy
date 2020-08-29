import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()

api_key = 'OY62azZFNJ1rJgeMy7G9DbPPiFiSADveqDSM7am4'

def fetchAsteroidNeowsFeed():
  URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"
  params = {
      'api_key':api_key,
      'start_date':'2020-01-22',
      'end_date':'2020-01-23'
  }
  response = requests.get(URL_NeoFeed,params=params).json()
  pp.pprint(response)
fetchAsteroidNeowsFeed()