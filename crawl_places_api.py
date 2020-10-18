import requests
import json
import time
import csv
from ristoranti_ire import r

CORSI = ["45.480137,9.210898",
         "45.456942,9.174997",
         "45.455820,9.196308",
         "45.479524,9.167362"]

TYPES = ["restaurant"]

RADIUS = '1000'  # km

FIELDS = ['name',
          'formatted_address',
          'international_phone_number',
          'website',
          'rating']

api_file = open('api_key.py', 'r')
API_KEY = api_file.read()
api_file.close()


class GooglePlaces(object):

    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey

    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
                 }
        res = requests.get(endpoint_url, params=params)
        results = json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params=params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
                 }
        res = requests.get(endpoint_url, params=params)
        place_details = json.loads(res.content)
        return place_details

if __name__ == '__main__':

    api = GooglePlaces(apiKey=API_KEY)
    restaurant_ls = []
    doppioni = [x.casefold() for x in r]

    for coordinates in CORSI:

        places = api.search_places_by_coordinate(location=coordinates,
                                                 radius=RADIUS,
                                                 types=TYPES)
        for place in places:
            details = api.get_place_details(place['place_id'], fields=FIELDS)
            name = details['result']['name'].casefold()
            if name not in doppioni:
                if not any(x in name for x in ['pizz', 'keba']):

                    restaurant_ls.append({k : details['result'].get(k, None)
                                          for k in FIELDS})
                    doppioni.append(name)

    with open('restaurants.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file,
                            fieldnames=restaurant_ls[0].keys())
        fc.writeheader()
        fc.writerows(restaurant_ls)
