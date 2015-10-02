import unittest
from application.driver import Driver
from mock import patch


class TestDriver(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    @patch('application.driver.time.sleep')
    def test_sleep(self, _):
        self.assertEqual(self.driver.sleep_time, 1) 

        self.driver._sleep()
        self.assertEqual(self.driver.sleep_time, 2) 

        self.driver._sleep()
        self.assertEqual(self.driver.sleep_time, 4)

    @patch('application.driver.time.sleep')
    def test_sleep_caps_at_max(self, _):
        self.driver.sleep_time = 20
        self.driver._sleep()
        self.assertEqual(self.driver.sleep_time, 30) 
  
