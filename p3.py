from itertools import permutations

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

ts = 'ccccccccccccssss'
print ts
x = 0
for p in unique_permutations(ts, 16):
		x = x + 1
		#print p
print x
