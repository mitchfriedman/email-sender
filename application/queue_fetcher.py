from application.email import Email
from siphon import Client
from siphon.queue import Queue


class EmailQueue(object):
    def __init__(self, siphon_client, queue_name):
        self.client = siphon_client
        self.queue_name = queue_name
        self.emails = Queue(self.client.Queues, self.queue_name)
    
    def fetch_email(self):
        email = self._siphon_dequeue()
        template = email.pop('template', None)
        return Email(template, **email)
    
    def _siphon_dequeue(self):
        return self.emails.dequeue()

