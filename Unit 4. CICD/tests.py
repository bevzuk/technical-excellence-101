# -*- coding: utf-8 -*-

import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        with open('build/Kolobok.html',mode='r') as output_file:
            self.html = output_file.read()

    def test_has_header(self):
        self.assertTrue('<h1>Сказка про колобка</h1>' in self.html)

    def test_has_rabbit(self):
        self.assertTrue('<h3>3.1 Заяц</h3>' in self.html)
        
    def test_has_wolf(self):
        self.assertTrue('<h3>3.2 Ночной Волк</h3>' in self.html)

    def test_has_bear(self):
        self.assertTrue('<h3>3.4 Медведь</h3>' in self.html)

if __name__ == '__main__':
    unittest.main()
