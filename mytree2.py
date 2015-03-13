import sys

def add_children(path, depth):
	if (depth == 1):
		yield path + ['-cl']
		yield path + ['-s']
		yield path + ['-cr']
	else:
		for p in add_children(path + ['-cl'], depth - 1): yield p
		for p in add_children(path + ['-s'], depth - 1): yield p
		for p in add_children(path + ['-cr'], depth - 1): yield p
	
def build_tree(depth):
	r = ['0']
	for path in add_children(r, depth):
		print(path)

depth = int(sys.argv[1])
build_tree(depth)
