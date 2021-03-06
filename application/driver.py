import time
from siphon import Client
from application.queue_fetcher import EmailQueue
from application.template_renderer import TemplateRenderer
from application.sender import Sender
import os


class Driver(object):

    _MAX_SLEEP_TIME = 30

    def __init__(self, config=None):
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
             
            email_body = templater.render(email.template, email.email_data)
            message = self.email_sender.build_email(email.email_data.get('to'),
                                                    email.email_data.get('subject'),
                                                    email_body)

            try:
                sender.send_email(template)
            except Exception as e:
                print(e)

    def _sleep(self):
        time.sleep(self.sleep_time)
        self.sleep_time = min(self.sleep_time * 2, self._MAX_SLEEP_TIME)



if __name__ == "__main__":
    driver = Driver()
    driver.drive()

