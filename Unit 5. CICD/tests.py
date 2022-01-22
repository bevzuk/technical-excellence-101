# -*- coding: utf-8 -*-

import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        with open('build/Kolobok.html', mode='r') as output_file:
            self.html = output_file.read()

    def test_has_header(self):
        self.assertTrue('<h1>Сказка про колобка</h1>' in self.html)


if __name__ == '__main__':
    unittest.main()
