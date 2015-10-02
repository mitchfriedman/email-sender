class Email(object):
    def __init__(self, template_name, template_data=None, email_data=None):
        self.template_name = template_name
        self.template_data = template_data or {}
        self.email_data = email_data or {}

