import unittest
from application.sender import Sender


class TestSender(unittest.TestCase):
    def setUp(self):
        self.sender = Sender({'SG_USERNAME': 'FOO', 'SG_PASSWORD': 'BAR', 'SG_SENDER': 'BAZ'})

    def test_correct_setup(self):
        self.assertEqual(self.sender._sg_username, 'FOO')
        self.assertEqual(self.sender._sg_password, 'BAR')
        self.assertEqual(self.sender._from_email, 'BAZ')
