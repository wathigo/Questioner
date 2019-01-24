""" Import the necessary modules """
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from instance.config import app_config
from dotenv import load_dotenv
from .db_config import table_queries

load_dotenv()
ENV = os.getenv('FLASK_ENV')
if ENV == 'testing':
    DB_URL = os.getenv('TESTDB_URL')
else:
    DB_URL = os.getenv('DATABASE_URL')


def db_conn():
    """" Create a database connection """
    connection = psycopg2.connect(os.getenv('TESTDB_URL'))
    return connection

def create_tables():
    """ Create the tables """
    connect = db_conn()
    cursor = connect.cursor()
    queries = table_queries()
    for sql in queries:
        cursor.execute(sql)
        connect.commit()
    cursor.close()

def insert_data():
    create_user = """INSERT INTO user_table(isadmin, firstname, lastname, username, \
                                      othername, email, password)
    VALUES (true, 'simon', 'wathigo', 'wathigosimon', 'kinuthia', \
            'wathigosimon@gmail.com', 'memory_Bad1') RETURNING userid;"""
    connection = db_conn()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(create_user)
    user = cursor.fetchone()
    userid = user['userid']
    create_meetup = """INSERT INTO meetups(userid, title, description, location, happeningon)
    VALUES ('%s', 'Entertainment', 'choreography', 'Sports Club', \
            '2015-08-23') RETURNING meetupid;""" % (userid)
    cursor.execute(create_meetup)
    meetup = cursor.fetchone()
    meetupid = meetup['meetupid']
    print(meetup)
    meetupid = meetup['meetupid']
    create_question = """INSERT INTO question(meetupid, userid, title, question, votes)
    VALUES ('%s', '%s', 'FloorNumber', 'Which floor are we going to meet?', 0)""" % \
    (meetupid, userid)
    cursor.execute(create_question)
    connection.commit()
    cursor.close()
