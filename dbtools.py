from DBconnect import connection_handler
from datetime import datetime

@connection_handler
def add_vote(cursor, username: str, planet: str):

    query = """SELECT vote_number FROM planet_votes WHERE planet=%(planet)s;"""
    variables = {'planet': planet}

    cursor.execute(query, variables)
    vote = cursor.fetchone()

    print(vote)
    print(type(vote))

    time = datetime.now()

    query = """INSERT INTO planet_votes (vote_number, username, time, planet)
               VALUES (%(vote)s), (%(username)s), (%(time)s), (%(planet)s);"""
    variables = {'vote': vote, 'username': username, 'time': time, 'planet': planet}


@connection_handler
def add_user(cursor, username: str, hashed_password: str):

    query = """INSERT INTO users (username, password) VALUES (%(username)s, %(hashed_password)s);"""
    variables = {'username': username, 'hashed_password': hashed_password}

    cursor.execute(query, variables)

@connection_handler
def get_user(cursor, username: str):

    query = """SELECT username, password FROM users WHERE username = %(username)s;"""
    variables = {'username': username}

    cursor.execute(query, variables)
    return cursor.fetchone()