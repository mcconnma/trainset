import itertools

ts = "c c c c c c c c c c c c s s s s".split()

perms = itertools.permutations(ts, r=8)
print len(list(perms))
