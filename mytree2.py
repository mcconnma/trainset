import sys

'''
preorder
In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree.
postorder
In a postorder traversal, we recursively do a postorder traversal of the left subtree and the right subtree followed by a visit to the root node.
inorder
In an inorder traversal, we recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree.
'''

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())


class Node:
	def __init__(self, key):
		self.key = key 
		self.children = []
	def addchild(self, child):
		self.children.append(child)
	def getkey(self):
		return self.key


#a3={:name=>"-cl", :children=>[]}
#a2={:name=>"-s", :children=>[]}
#a1={:name=>"-cr", :children=>[b1,b2,b3]}

#a={:name=>"0", :children=>[a1,a2,a3]}

'''
def paths(node,path='',&proc):

  if node[:children].empty?
    proc.call(path+node[:name])
  else
    node[:children].each{|c| paths(c,path+node[:name],&proc)}


	for d in range(depth, 0, -1):
		for n in range(0,3**d):
			x = chr(64+d) + str(n+1)
			yield x


paths(a) {|path| puts path }
'''

	#print 'add: ' + parent.getkey() + ', d: ' + str(depth)
def add_children(path, depth):

	if (depth == 1):
		path.append('-cl')
		yield path
		path.pop()

		path.append('-s')
		yield path
		path.pop()

		path.append('-cr')
		yield path
		path.pop()

	else:
		print path
		for p in add_children(path + ['-cl'], depth - 1): yield p
		for p in add_children(path + ['-s'], depth - 1): yield p
		for p in add_children(path + ['-cr'], depth - 1): yield p
	
def build_tree(depth):
	r = ['0']
	for path in add_children(r, depth):
		print(path)

depth = int(sys.argv[1])
build_tree(depth)

def test():
	r = Node('a')
	r.insertLeft('b1')
	b1 = r.getLeftChild()
	b1.insertLeft('c1')
	b1.insertRight('c2')

	preorder(r)
	print '-'
	postorder(r)
	print '-'
	inorder(r)
