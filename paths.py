

class Node:
	def __init__(self, name):
		self.value = name
		self.children = []
	def add(self, node):
		self.children.append(node)	

def paths(tree):
	if (len(tree.children) == 0):
		return ([])
	else:
		root = tree.value
		rooted_paths = []
		for subtree in tree.children:
				useable = paths(subtree)
				for path in useable:
						rooted_paths.append([root]+path)
		return rooted_paths

if __name__ == "__main__":

	root = Node('0')
	a = Node('a') 
	b = Node('b') 
	root.add(a)
	root.add(b)
	c = Node('c') 
	a.add(c)
		
	a = paths(root)
	print a
