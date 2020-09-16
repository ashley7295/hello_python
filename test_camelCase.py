import unittest

import camelCase

from unittest import TestCase

class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):

        self.assertEqual("helloWorld", camelCase.camelcase("Hello World"))

    def test_space(self):    
        
        self.assertEqual("", camelCase.camelcase(""))
        

if __name__ == "__main__":
    unittest.main() 