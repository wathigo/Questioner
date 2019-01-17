""" Import the necessary modules """
import os
import psycopg2
from dotenv import load_dotenv
from .db_config import Tables

load_dotenv() ### Add the variables in the .env file to the enviroment
DB_URL = os.getenv('DATABASE_URL')


def db_conn():
    """" Create a database connection """
    connection = psycopg2.connect(DB_URL)
    return connection

def create_tables():
    """ Create the tables """
    connect = db_conn()
    cursor = connect.cursor()
    database = Tables()
    queries = database.table_queries()
    for sql in queries:
        cursor.execute(sql)
        connect.commit()
    cursor.close()
