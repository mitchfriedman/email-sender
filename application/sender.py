import sendgrid


class Sender(object):
    def __init__(self, email_configuration):
        self._from_email = email_configuration.get('SG_SENDER', None)

        self._sg_username = email_configuration.get('SG_USERNAME', None)
        self._sg_password = email_configuration.get('SG_PASSWORD', None)
        self.sg_client = sendgrid.SendGridClient(self._sg_username, self._sg_password, raise_errors=True)
        
    def send_email(self, email):
        try:
            status, msg = self.sg_client.send(email) 
        except SendGridClientError as e:
            raise e
        except SendGridServerError as e:
            raise e
    
    def build_email(self, to, subject, body):
        if self._sg_username == None or self._sg_password == None:
            raise Exception("You must use valid SendGrid credentials to send emails")
        mail = sendgrid.Mail(to=to, subject=subject, text=body, html=body, from_email = self._from_email)

        return mail
