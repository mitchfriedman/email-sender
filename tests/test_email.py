import unittest
from application.email import Email


class TestEmail(unittest.TestCase):
    def test_create_email_empty_data(self):
        email = Email("template.html")
        self.assertEqual(email.template_name, 'template.html') 
        self.assertEqual(email.template_data, {})
        self.assertEqual(email.email_data, {})

    def test_create_email_no_email_data(self):
        email = Email("template.html", template_data={'foo':"bar", 'bar':"bazzar"})
        self.assertEqual(email.template_name, 'template.html') 
        self.assertEqual(email.template_data['foo'], 'bar')
        self.assertEqual(email.template_data['bar'], 'bazzar')
        self.assertEqual(email.email_data, {})
    
    def test_email_full_data(self):
        template_data = {
            "foo": "bar",
            "Mitch_is": "Awesome"
        }
        email_data = {
            "to": "test@email.com",
            "subject": "Welcome to the party!",
        }
        
        email = Email("template.html", template_data, email_data)
        self.assertEqual(email.template_data['foo'], 'bar')
        self.assertEqual(email.template_data['Mitch_is'], 'Awesome')

        self.assertEqual(email.email_data['to'], 'test@email.com')
        self.assertEqual(email.email_data['subject'], 'Welcome to the party!')

