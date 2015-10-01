import unittest
from application.email import Email


class TestEmail(unittest.TestCase):
    def test_create_email_no_kwargs(self):
        email = Email("template.html")
        attrs = [attr for attr in dir(email) if not attr.startswith('_')]
        self.assertEqual(attrs, ['template'])

    def test_create_email_with_kwargs(self):
        email = Email("template.html", foo="bar", baz="bazzar")
        self.assertTrue(email.foo, "bar")
        self.assertTrue(email.baz, "bazzar")

