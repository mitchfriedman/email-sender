import unittest
import os
from application.template_renderer import TemplateRenderer


class TestRenderer(unittest.TestCase):
    
    def setUp(self):
        self._template_dir = 'tests/templates/'
        self.template_renderer = TemplateRenderer(self._template_dir)

    def _get_template_dir(self):
        return os.path.abspath(self._template_dir)

    def test_template_path(self):
        template_dir = self._get_template_dir()
        
        self.assertEqual(self.template_renderer.template_dir, template_dir)

    def test_get_template_file_path(self):
        template_dir_path = self._get_template_dir()
        template_file = 'foo.html'

        self.assertEqual(self.template_renderer.get_template_path(template_file), 
                template_dir_path + '/' + template_file)

    def test_get_raw_template(self):
        raw_template = self.template_renderer._get_raw_template('test1.html')

        self.assertEqual(raw_template, 'Hello Mr. Foo')

    def test_format_template(self):
        data = {'bar': 'Foo'}
        formatted = self.template_renderer.render('test1.html', data)

        self.assertEqual(formatted, 'Hello Mr. Foo')

