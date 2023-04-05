#! /usr/bin/env python3

import unittest

from main import convert_filename

class TestMain(unittest.TestCase):
    def test_wrong_filename(self):
        self.assertEqual('file_1.txt', convert_filename('file 1.txt'))
        self.assertEqual('file_abc.txt', convert_filename('file abc.txt'))

if __name__ == '__main__':
    unittest.main()