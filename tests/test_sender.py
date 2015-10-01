import unittest
from application.sender import Sender
from nose.tools import raises


class TestSender(unittest.TestCase):
    def setUp(self):
        self.sender = Sender({'SG_USERNAME': 'FOO', 'SG_PASSWORD': 'BAR', 'SG_SENDER': 'BAZ'})
        self.sender._sg_userame = 'FOO'
        self.sender._sg_password = 'BAR'

    def test_correct_setup(self):
        self.assertEqual(self.sender._sg_username, 'FOO')
        self.assertEqual(self.sender._sg_password, 'BAR')
        self.assertEqual(self.sender._from_email, 'BAZ')

    def test_build_email(self):
        email = self.sender.build_email("test_to", "test_subject", "test_body")
        self.assertEqual(email.to, ["test_to"])
        self.assertEqual(email.subject, "test_subject")
        self.assertEqual(email.html, "test_body")
    
    @raises(Exception)
    def test_build_email_invalid_sg_username(self):
        self._sg_username = None
        self.build_email("foo", "bar", "baz")
        self.assertTrue(False)
        
    @raises(Exception)
    def test_build_email_invalid_sg_password(self):
        self._sg_password = None
        self.build_email("foo", "bar", "baz")
        self.assertTrue(False)
        
