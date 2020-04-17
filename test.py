#!/usr/bin/python2.7

import random
import unittest
from trackbuilder import TrackBuilder
import glob
import os

class TestPaths(unittest.TestCase):

    @classmethod
    def remove(cls):
        files = glob.glob('*.png')
        for s in files:
            os.remove(s)

    @classmethod
    def setUpClass(cls):
        TestPaths.remove()

    @classmethod
    def tearDownClass(cls):
        TestPaths.remove()

    def setUp(self):
        self.tb = TrackBuilder()

    def test1(self):
        self.tb.id = 1
        path = "s cr s cr s cr s cr s cr s cr s cr s cr".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test2(self):
        self.tb.id = 5
        path = "cl cl cl cl cl cl cl cl".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test3(self):
        self.tb.id = 3
        path = "s cl s cl s cl s cl s cl s cl s cl s cl".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test4(self):
        self.tb.id = 4
        path = "cl s cl s cl s cl s cl s cl s cl s cl s".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test5(self):
        self.tb.id = 6
        path = "cr cr cr cr cr cr cr cr".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test6(self):
        self.tb.id = 2
        path = "cr s cr s cr s cr s cr s cr s cr s cr s".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test7(self):
        self.tb.id = 7
        path = "cr cr cr cr s cr cr cr cr s".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test8(self):
        self.tb.id = 8
        path = "cl cl cl cl s cl cl cl cl s".split()
        self.tb.reset_ctx(path)
        self.assertTrue(self.tb.build(path))

    def test9(self):
        self.tb.id = 9
        # doesn't get back
        path = "cr cr cr cr s s cr cr cr s cr cr cl".split()
        self.tb.reset_ctx(path)
        self.assertFalse(self.tb.build(path))

    def test10(self):
        self.tb.id = 10
        # doesn't get back
        path = "cr cr cr cr cl cr cr cr s cr cr cr cl".split()
        self.tb.reset_ctx(path)
        self.assertFalse(self.tb.build(path))

if __name__ == '__main__':
    unittest.main()
