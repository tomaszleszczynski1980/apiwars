from flask import Flask, render_template, redirect, request, url_for, session, json
from os import urandom
from DBconnect import test_connection
import requests
import dbtools
import utils


app = Flask(__name__)
app.secret_key = urandom(16)


def check_if_logged():
    if 'user' in session:
        user = session['user']
    else:
        user = None

    return user


@app.route('/')
@app.route('/<int:page>')
def main(page=None):

    if not page:
        page = 1

    user = check_if_logged()
    error = not test_connection()
    planets = requests.get(f'http://swapi.dev/api/planets/?page={page}').json()['results']

    keys_list = ['name', 'diameter', 'climate', 'terrain', 'surface_water', 'population', 'residents']

    for planet_index, planet in enumerate(planets):
        new_planet = utils.filter_dict(planet, keys_list)
        planets[planet_index] = new_planet

    return render_template("main.html", planets=planets, user=user, error=error)


if __name__ == '__main__':
    app.run()
