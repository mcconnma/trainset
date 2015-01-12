

tracks = 'c s c'.split()
tracks = '1 2 3'.split()

def search():
	print('search')
	for t in tracks:
		yield t

g = search()
print(next(g))
print(next(g))
print(next(g))

