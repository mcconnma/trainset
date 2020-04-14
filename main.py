#!/usr/bin/python

import sys
import os
import glob
import cProfile
from trackbuilder import TrackBuilder

solutions = []
NUM_CL = 6
NUM_CR = 6
NUM_S = 4

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

def valid(path):
	t1 = True
	# check for valid use of 's'
	if path.count('s') >= 3:
		l2 = ''.join(path * 2)
		if l2.find('ss') == -1:
			t1 = False
	# the curves are reversible so we need to check that number <= cl + cr
	t2 = (path.count('cl') + path.count('cr') <= NUM_CL + NUM_CR) and path.count('s') <= NUM_S
	return t1 and t2

def removefiles(depth):
	files = glob.glob(depth + '*.png')
	for file in files:
		os.remove(file)

def testpath(tb, path):
	start_point = tb.getCurrentPoint()
	start_deg = tb.getCurrentDegree()
	tb.buildit(path)
	end_point = tb.getCurrentPoint()
	end_deg = tb.getCurrentDegree()
	return start_point == end_point and start_deg == end_deg

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
	tb = TrackBuilder()
	for path in add_children(r, depth):
		i = i+1
		tb.init(path)
		if not valid(path):
			continue
		if testpath(tb, path):
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
