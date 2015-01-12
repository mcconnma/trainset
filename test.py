#!/usr/bin/python3


import random
import unittest
from draw import TrackBuilder

  #pieces = "cr cr cr cr cr cr s s cl cl cl cl cl cl s s".split()
  #pieces = "cr cr cr cr cr cr s s cl cl cl cl cl cl s s".split()
  #pieces = "cr cr cr cr cl cr cr cr s cr cr cr cl".split() # doesnt get back
  #pieces = "cr cr cr cr s s cr cr cr s cr cr cl".split() # doesnt get back
  #pieces = "c c c c c c c c ".split()
  #pieces = "c c c c s c c c c s".split()
  #pieces = "s cr s cr s cr s cr s cr s cr s cr".split()
  #pieces = "s cr s cr s cr s cr s cr".split()
  #pieces = "cr s cr s cr s cr s cr s cr s cr s cr s".split()
  #pieces = "s cr s cr s cr s cr s cr s cr s cr s cr".split()
  #pieces = "cl s cl s cl s cl s cl s cl s cl s cl s".split()
  #pieces = "cl s cl s cl s cl s cl s cl s cl s cl s ".split()
  #pieces = "s cl s cl s cl s cl s cl s cl s cl s cl ".split()
  #pieces = "s cr s cr s cr s cr s cr s cr s cr s cr".split()


class TestPaths(unittest.TestCase):

	def setUp(self):
		self.tb = TrackBuilder()
		self.startpoint = self.tb.getCurrentPoint()

	def tearDown(self):
		print('current after test: ', self.tb.getCurrentPoint())

	def test1(self):
		self.tb.buildit("s cr s cr s cr s cr s cr s cr s cr s cr".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test2(self):
		self.tb.buildit("cr s cr s cr s cr s cr s cr s cr s cr s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test3(self):
		self.tb.buildit("s cl s cl s cl s cl s cl s cl s cl s cl".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test4(self):
		self.tb.buildit("cl s cl s cl s cl s cl s cl s cl s cl s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test5(self):
		self.tb.buildit("cl cl cl cl cl cl cl cl".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test6(self):
		self.tb.buildit("cr cr cr cr cr cr cr cr".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test7(self):
		self.tb.buildit("cr cr cr cr s cr cr cr cr s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test8(self):
		self.tb.buildit("cl cl cl cl s cl cl cl cl s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

if __name__ == '__main__':
    unittest.main()
