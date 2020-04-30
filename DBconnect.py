import os
import psycopg2
import psycopg2.extras


def get_connection_url():

    user = os.environ.get('PSQL_USER')
    password = os.environ.get('PSQL_PASS')
    host = os.environ.get('PSQL_HOST')
    dbname = os.environ.get('PSQL_DB')

    if user and password and host and dbname:
        return f"postgresql://{user}:{password}@{host}/{dbname}"
    else:
        # raise ConnectionError("Necessary environment variable(s) not defined")
        return f"postgresql://Tomek:kremlin@localhost/apiwars"


def open_db():

    try:
        connection = psycopg2.connect(get_connection_url())
        connection.autocommit = True
    except psycopg2.DatabaseError as error:
        print('Database connection error:', error)
        raise ConnectionError

    return connection


def test_connection():

    try:
        connection = open_db()
        connection.close()
    except ConnectionError:
        return False

    return True


def connection_handler(function):

    def wrapper(*args, **kwargs):
        connection = open_db()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return_object = function(cursor, *args, **kwargs)
        cursor.close()
        connection.close()
        return return_object

    return wrapper
