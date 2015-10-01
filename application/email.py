class Email(object):
    def __init__(self, template_name, **kwargs):
        self.template = template_name
        for k, v in kwargs.items():
            setattr(self, k, v)

