#!/usr/bin/python

import sys
import os
import glob
import cProfile
from trackbuilder import TrackBuilder

solutions = []

def add_children(path, depth):
	if (depth == 1):
		yield path + ['cl']
		yield path + ['s']
		yield path + ['cr']
	else:
		for p in add_children(path + ['cl'], depth - 1): yield p
		for p in add_children(path + ['s'], depth - 1): yield p
		for p in add_children(path + ['cr'], depth - 1): yield p

def convert(i):
	if i == 's':
		return i
	elif i == 'cl':
		return 'cr'
	elif i == 'cr':
		return 'cl'

def duplicate(path):

	# rotate list, check for duplicates
	for x in range(1,5):
		p = path[x:]+path[:x]
		if solutions.count(p) == 1:
			return True

	# check for mirror images
	convertedpath = [convert(x) for x in path]
	for x in range(0,5):
		p = convertedpath[x:]+convertedpath[:x]
		if solutions.count(p) == 1:
			return True

def truncatepath(path):
	return str.join('', path)

def valid(l):
	NUM_CL	= 6
	NUM_CR	= 6
	NUM_S		= 4
	return (l.count('cl') + l.count('cr') <= NUM_CL + NUM_CR) and l.count('s') <= NUM_S 	

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

def build_tree(depth):
	r = []
	i = 0
	for path in add_children(r, depth):
		i = i+1
		if not valid(path):
			continue
		if duplicate(path):
			continue
		tb = TrackBuilder(str(path))
		if testpath(tb, path):
			solutions.append(path)
			imageid = str(depth) + '-' + str(i)
			tb.createImage(imageid)
			print(str(imageid) + ':' + str(path))
	print("total checked: " + str(i))

depth = int(sys.argv[1])
removefiles(str(depth))
cProfile.run('build_tree(depth)')
