#!/usr/bin/python

import sys
import os
import glob
import cProfile
from trackbuilder import TrackBuilder

solutions = []

def removefiles(depth):
	files = glob.glob(depth + '*.png')
	for file in files:
		os.remove(file)


def convert(i):
	if i == 's':
		return i
	elif i == 'cl':
		return 'cr'
	elif i == 'cr':
		return 'cl'

# this could be made more efficient ...
def duplicate(path):
	s2 = ''.join(path)
	cpath = [convert(x) for x in path]
	s2cpath = ''.join(cpath)
	for s in solutions:
		s1 = ''.join(s*2)
		# check dups
		if s1.find(s2) != -1:
			return True
		# check mirrors
		if s1.find(s2cpath) != -1:
			return True
	return False



def add_children(path, depth):
	if depth == 1:
		yield path + ['cl']
		yield path + ['s']
		yield path + ['cr']
	else:
		for p in add_children(path + ['cl'], depth - 1):
			yield p
		for p in add_children(path + ['s'], depth - 1):
			yield p
		for p in add_children(path + ['cr'], depth - 1):
			yield p

def build_tree(depth):

	r = []
	i = 0

	tb = TrackBuilder(None)

	for path in add_children(r, depth):

		i = i+1
		tb.set_path(path)

		if not tb.is_valid_path():
			continue
		start_point = tb.getCurrentPoint()
		start_deg = tb.getCurrentDegree()
		tb.buildit()
		end_point = tb.getCurrentPoint()
		end_deg = tb.getCurrentDegree()
		if start_point == end_point and start_deg == end_deg:
			if duplicate(path):
				continue
			solutions.append(path)
			imageid = str(depth) + '-' + str(i)
			tb.createImage(imageid)
			print(str(imageid) + ':' + str(path))
	print("total checked: " + str(i))

tree_depth = int(sys.argv[1])
removefiles(str(tree_depth))
# cProfile.run('build_tree(tree_depth)')
build_tree(tree_depth)
