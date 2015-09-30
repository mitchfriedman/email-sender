import os
from jinja2 import Template


class TemplateRenderer(object):

    def __init__(self, template_dir):
        self.template_dir = os.path.abspath(template_dir)

    def _get_raw_template(self, template_name):
        raw_template = open(os.path.join(self.template_dir, template_name)).read()
        return raw_template.strip()

    def get_template_path(self, template_name):
        return os.path.join(self.template_dir, template_name)
    
    def render(self, template_name, data):
        raw_template = self._get_raw_template(template_name)
        template = Template(raw_template)
        return template.render(**data)
        
