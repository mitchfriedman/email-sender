import unittest
from mock import patch
from siphon import Client
from application.queue_fetcher import EmailQueue


class TestEmailQueue(unittest.TestCase):
    def setUp(self):
        self.email_queue = EmailQueue(Client('http://127.0.0.1:8000'), 'emails')

    def test_queue_uri(self):
        self.assertEqual(self.email_queue.queue_name, 'emails')
    
    @patch("application.queue_fetcher.EmailQueue._siphon_dequeue")
    def test_fetch_email(self, dequeue):
        dequeue.return_value = {
            'template': 'template_1.html',
        }
        email = self.email_queue.fetch_email()
        self.assertEqual(email.template, 'template_1.html')

