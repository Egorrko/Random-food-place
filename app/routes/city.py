import re

from flask import render_template

from app import config
from app.common import get_places

from . import routes


@routes.route("/city/<string:city>")
def city(city):
    if not re.match("^[A-Za-zА-ЯёЁа-я- ]*$", city):  # check if city name is valid
        return render_template('index.html', alert_text="Wrong city name", config=config)  # if not - display error
    places = get_places(city)
    if not places or len(places) == 1:
        return render_template('index.html', alert_text=places[0], config=config)  # if error
    return render_template('places.html', places=places, city=city, config=config)
