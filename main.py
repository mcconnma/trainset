#!/usr/bin/python

import sys
import os
import glob
import multiprocessing
import cProfile
from trackbuilder import TrackBuilder

solutions = []
piece_converter = {'s': 's', 'cl': 'cr', 'cr': 'cl'}

def duplicate(path):

	s2 = ''.join(path)
	cpath = [piece_converter[x] for x in path]
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

class TrackBuilderItem(object):
	__slots__ = ['path_id', 'path']
	def __init__(self, path_id, path):
		self.path_id = path_id
		self.path = path

class TrackBuilderConsumer(multiprocessing.Process):

	def __init__(self, task_queue, result_queue):
		multiprocessing.Process.__init__(self)
		self.task_queue = task_queue
		self.result_queue = result_queue
		self.tb = TrackBuilder()

	def run(self):
		while True:
			items = self.task_queue.get()
			if items is None:
				self.task_queue.task_done()
				break
			for item in items:
				self.tb.reset_ctx(item.path)
				# if the path completed successfully, add to result queue
				if self.tb.build(item.path):
					self.result_queue.put(item)
			self.task_queue.task_done()
		return

def build_tree(path, depth):
	""" Use generators to create the path """
	if depth == 1:
		yield path + ['cl']
		yield path + ['s']
		yield path + ['cr']
	else:
		for p in build_tree(path + ['cl'], depth - 1):
			yield p
		for p in build_tree(path + ['s'], depth - 1):
			yield p
		for p in build_tree(path + ['cr'], depth - 1):
			yield p

def main():

	total_processed = 0
	total_valid = 0
	tree_depth = int(sys.argv[1])
	task_list = list()

	# remove any existing path images
	files = glob.glob("%d*.png" % tree_depth)
	for file in files:
		os.remove(file)

	# create the task and result queues
	tasks = multiprocessing.JoinableQueue()
	result_queue = multiprocessing.Queue()

	# setup consumers and start
	num_consumers = multiprocessing.cpu_count()
	consumers = [TrackBuilderConsumer(tasks, result_queue) for i in range(num_consumers)]
	for w in consumers:
		w.start()

	# generate paths and add to process queue
	for path in build_tree([], tree_depth):
		total_processed += 1
		if not TrackBuilder.is_valid_path(path):
			continue
		total_valid += 1
		task_list.append(TrackBuilderItem(total_processed, path))
		if len(task_list) % 1000 == 0:
			tasks.put(task_list)
			task_list = list()

	# likely not finished processing
	if len(task_list) > 0:
			tasks.put(task_list)

	# add poison pills
	for i in range(num_consumers):
		tasks.put(None)

	# wait for tasks
	tasks.join()

	# process result queue
	tb = TrackBuilder()
	while not result_queue.empty():
		result = result_queue.get()
		path = result.path
		path_id = result.path_id
		if duplicate(path):
			continue
		solutions.append(path)
		tb.reset_ctx(path)
		imageid = "%d-%d" % (tree_depth, path_id)
		tb.create_image(imageid)
		print("%s:%r" % (imageid, path))

	print("num_processed: %d" % total_processed)
	print("total_valid: %d" % total_valid)

# cProfile.run('main()')
main()
