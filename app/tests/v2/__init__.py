""" Import the necessary modules """
import unittest
from flask import json
from app import create_app
from ...utils.database import db_conn
import os
from ...utils.database.db_config import drop_table_query
from run import appl

class BaseTests(unittest.TestCase):
    """ set up environment for running tests"""
    def setUp(self):
        appl.testing = True
        os.environ['FLASK_ENV'] = 'testing'
        self.app = create_app()
        self.client = self.app.test_client()
        return self.client

    def tearDown(self):
        queries = drop_table_query()
        connection = db_conn()
        cursor = connection.cursor()
        for sql_query in queries:
            cursor.execute(sql_query)
            connection.commit()
