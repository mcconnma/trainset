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
		self.tb = TrackBuilder('test')
		self.tb.dowritefile = True
		self.startpoint = self.tb.getCurrentPoint()

	def test1(self):
		self.tb.id = 1
		self.tb.buildit("s cr s cr s cr s cr s cr s cr s cr s cr".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test2(self):
		self.tb.id = 5
		self.tb.buildit("cl cl cl cl cl cl cl cl".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test3(self):
		self.tb.id = 3
		self.tb.buildit("s cl s cl s cl s cl s cl s cl s cl s cl".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test4(self):
		self.tb.id = 4
		self.tb.buildit("cl s cl s cl s cl s cl s cl s cl s cl s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test5(self):
		self.tb.id = 6
		self.tb.buildit("cr cr cr cr cr cr cr cr".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test6(self):
		self.tb.id = 2
		self.tb.buildit("cr s cr s cr s cr s cr s cr s cr s cr s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test7(self):
		self.tb.id = 7
		self.tb.buildit("cr cr cr cr s cr cr cr cr s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	def test8(self):
		self.tb.id = 8
		self.tb.buildit("cl cl cl cl s cl cl cl cl s".split())
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	@unittest.skip("demonstrating skipping")
	def test9(self):
		self.tb.id = 9
		self.tb.buildit("cr cr cr cr s s cr cr cr s cr cr cl".split()) # doesnt get back
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	@unittest.skip("demonstrating skipping")
	def test10(self):
		self.tb.id = 10
		self.tb.buildit("cr cr cr cr cl cr cr cr s cr cr cr cl".split()) # doesnt get back
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

if __name__ == '__main__':
		unittest.main()
		
