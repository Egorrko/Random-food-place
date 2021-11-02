import json
import random

import requests

from app import config


def get_places(city):
    # returns list of places or error
    url = (f"https://search-maps.yandex.ru/v1/?text={city},Еда&"
           f"type=biz&results=500&lang=ru_RU&apikey={config.PLACES_API_KEY}")
    r = requests.get(url)
    # get places using Yandex API
    if r.status_code != 200:
        return [r.text]  # error
    data = json.loads(r.text)
    if len(data["features"]) < config.PLACES_COUNT:
        return ['Places not found']  # places not found
    json_places = random.sample(data["features"], k=config.PLACES_COUNT)

    places = []
    for place in json_places:
        categories = " ".join([category['name'] for category in place['properties']['CompanyMetaData']['Categories']])
        # create string of categories
        coordinates = place['geometry']['coordinates'][::-1]
        places.append([place['properties']['name'], categories, place['properties']['description'], coordinates])
    return(places)