from siphon import Client
from siphon.queue import Queue


class EmailQueue(object):
    def __init__(self, siphon_client, queue_name):
        self.client = siphon_client
        self.queue_name = queue_name
        self.emails = Queue(self.client.Queues, self.queue_name)
    
    def fetch(self):
        return self.emails.dequeue()
    

