# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import hello_world

# so does using unittest mean it always needs to be instantiated with an object?

class hworldtests(unittest.TestCase):

    def test_hello_no_name(self):
        self.assertEqual( # nice multi line situation you got here
            'Hello, World!', # expected behavior
            hello_world.hello() # hello_world.py module, hello() func w no args
        )

    def test_hello_name_given(self):
        self.assertEqual(
            'Hello, Ol Eleven Bearings!', # will use whatever we put in for the test!
            hello_world.hello('Ol Eleven Bearings')
        )

    def test_hello_utf_brayka(self):
        self.assertEqual(
            'Hello, Evgénya!',
            hello_world.hello('Evgénya')
        )

    def test_hello_o_thor(self):
        self.assertEqual(
            'Hello, BOBZOR!',
            hello_world.hello('BOBZOR')
        )

if __name__ == '__main__':
    unittest.main()     
