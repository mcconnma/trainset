#!/usr/bin/python3

import random
import unittest
from draw import TrackBuilder
from PIL import Image

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
		self.tb.dowrite = True
		self.startpoint = self.tb.getCurrentPoint()

	def tearDown(self):
		print('current after test: ', self.tb.getCurrentPoint())

	@classmethod
	def tearDownClass(cls):
		blank_image = Image.new("RGB", (1050, 350))
		im1 = Image.open('example1.png')
		im2 = Image.open('example2.png')
		im3 = Image.open('example3.png')
		blank_image.paste(im1, (0,0))
		blank_image.paste(im2, (350,0))
		blank_image.paste(im3, (700,0))
		blank_image.show()

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

	@unittest.skip("demonstrating skipping")
	def test9(self):
		self.tb.buildit("cr cr cr cr s s cr cr cr s cr cr cl".split()) # doesnt get back
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

	@unittest.skip("demonstrating skipping")
	def test9(self):
		self.tb.buildit("cr cr cr cr cl cr cr cr s cr cr cr cl".split()) # doesnt get back
		self.assertTrue(self.startpoint == self.tb.getCurrentPoint())

if __name__ == '__main__':
		unittest.main()
		
