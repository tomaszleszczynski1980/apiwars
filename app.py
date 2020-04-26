from flask import Flask, render_template, redirect, request, url_for, session, json
from os import urandom
from DBconnect import test_connection
import dbtools
import auth


app = Flask(__name__)
app.secret_key = urandom(16)


def check_if_logged():

    if 'player' in session:
        player = session['player']
    else:
        player = None

    return player


@app.route('/')
def main():

    error = not test_connection()

    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True)
