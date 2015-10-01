import time
from siphon import Client
from application.queue_fetcher import EmailQueue
import os


class Driver(object):

    _MAX_SLEEP_TIME = 30

    def __init__(self, config):
        self.sleep_time = 1
        self.queue = EmailQueue(Client('http://127.0.0.1:8000'), 'emails')
        self.template_renderer = TemplateRenderer('templates/')
        self.email_sender = Sender({'SG_USERNAME': os.environ.get('SG_USERNAME'),
                                    'SG_PASSWORD': os.environ.get('SG_PASSWORD'),
                                    'SG_SENDER': os.environ.get('SG_SENDER'),
                                    })

    def drive(self):
        while True:
            email = self.emails_queue.dequeue()
            if not email:
                self.sleep()
                continue
            
            template = templater.generate(email)
            sender.send(template)

    def _sleep(self):
        time.sleep(self.sleep_time)
        self.sleep_time = max(self.sleep_time * 2, self._MAX_SLEEP_TIME)



if __name__ == "__main__":
    driver = Driver()
    driver.drive()

