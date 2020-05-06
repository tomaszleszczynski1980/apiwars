from flask import Flask, render_template, redirect, request, url_for, session, json, jsonify
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
    response = requests.get(f'https://swapi.dev/api/planets/?page={page}').json()
    planets = response['results']
    prev = response['previous']
    nextt = response['next']

    keys_list = ['name', 'diameter', 'climate', 'terrain', 'surface_water', 'population', 'residents']

    for planet_index, planet in enumerate(planets):
        filtered_planet = utils.filter_dict(planet, keys_list)
        planets[planet_index] = filtered_planet

    return render_template("main.html", planets=planets, user=user, error=error, prev=prev, nextt=nextt)


@app.route('/residents/<planet>')
def get_residents(planet):

    user = check_if_logged()
    error = not test_connection()

    planet = planet.replace(' ', '%20')
    response = requests.get(f'https://swapi.dev/api/planets/?search={planet}').json()
    residents = response['results'][0]['residents']

    keys_list = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender']
    residents_list = []

    for resident_url in residents:
        response_resident = requests.get(resident_url).json()
        filtered_resident = utils.filter_dict(response_resident, keys_list, return_list=True)
        residents_list.append(filtered_resident)

    return jsonify(residents_list)


@app.route('/vote/<planet>')
def vote(planet):

    user = check_if_logged()
    connection = test_connection()

    if connection and user:
        dbtools.add_vote(user, planet)
        return jsonify(vote=True)
    else:
        return jsonify(vote=False)


@app.route('/register')
def register():

    pass


@app.route('/login')
def login():

    user = check_if_logged()
    connection = test_connection()
    

if __name__ == '__main__':
    app.run()
