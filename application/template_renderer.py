import os
from jinja2 import Template


class TemplateRenderer(object):

    def __init__(self, template_dir):
        self.template_dir = os.path.abspath(template_dir)

    def render(self, template_name, data):
        raw_template = open(os.path.join(self.template_dir, template_name)).read()
        return raw_template.strip()
        #template = Template(

    def get_template_path(self, template_name):
        return os.path.join(self.template_dir, template_name)
    
