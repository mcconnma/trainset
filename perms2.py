#!/usr/bin/python3


def permutations(ls):
    if len(ls) == 1: yield ls
    for i in range(len(ls)):
        for p in permutations(ls[:i]+ls[i+1:]):
            yield [ls[i]]+p

ls = 'c c c c c c c c c c c c'.split()
ls = 'c c c c c c c c c c'.split()
c = 0
for p in permutations(ls):
	c = c+1
    #print(p)

print('count: ', c)
