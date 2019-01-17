""" Import the necessary modules """
import unittest
from app import create_app

from run import appl

class BaseTests(unittest.TestCase):
    """ set up environment for running tests"""
    def setUp(self):
        appl.testing = True
        self.app = create_app()
        self.client = self.app.test_client()
        return self.client
