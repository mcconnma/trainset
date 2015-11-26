#!/usr/bin/python3.4

import concurrent.futures
import math
from trackbuilder import TrackBuilder

def doit(path):
	tb = TrackBuilder()
	tb.init(path)
	start_point = tb.getCurrentPoint()
	start_deg = tb.getCurrentDegree()
	tb.buildit(path)
	end_point = tb.getCurrentPoint()
	end_deg = tb.getCurrentDegree()
	return start_point == end_point and start_deg == end_deg

executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)
path = "s cr s cr s cr s cr s cr s cr s cr s cr".split()
f = executor.submit(doit, path)
print(f.result())
