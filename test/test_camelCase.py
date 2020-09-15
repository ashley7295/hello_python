

import camelCase
from unittest import TestCase



class TestCamelCase(TestCase):
    def test_camcelcase_sentence(self):
        self.assertEqual("helloWorld", camelcase.camel_case("Hello World"))