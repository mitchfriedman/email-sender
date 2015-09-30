import time


class Driver(object):

    _MAX_SLEEP_TIME = 30

    def __init__(self, config):
        self.sleep_time = 1

    def _sleep(self):
        time.sleep(self.sleep_time)
        self.sleep_time = max(self.sleep_time * 2, self._MAX_SLEEP_TIME)

    def drive(self):
        while True:
            email = self.emails_queue.dequeue()
            if not email:
                self.sleep()
                continue
            
            template = templater.generate(email)
            sender.send(template)



driver = Driver()
driver.drive()

