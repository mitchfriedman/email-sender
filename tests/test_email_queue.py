import unittest
from siphon import Client
from application.email_queue import EmailQueue


class TestEmailQueue(unittest.TestCase):
    def setUp(self):
        self.email_queue = EmailQueue(Client('http://127.0.0.1:8000'), 'emails')

    def test_queue_uri(self):
        self.assertEqual(self.email_queue.queue_name, 'emails')


