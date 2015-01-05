def permutations(ls):
    if len(ls) == 1: yield ls
    for i in xrange(len(ls)):
        for p in permutations(ls[:i]+ls[i+1:]):
            yield [ls[i]]+p

ls = 'c c s'.split()
for p in permutations(ls):
    print(p)
