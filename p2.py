#!/usr/bin/env python

__version__ = "1.0"

"""xpermutations.py
Generators for calculating a) the permutations of a sequence and
b) the combinations and selections of a number of elements from a
sequence. Uses Python 2.2 generators.

Similar solutions found also in comp.lang.python

Keywords: generator, combination, permutation, selection

See also: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/105962
See also: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66463
See also: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66465
"""

#from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

ts = 'c c c c c c c c s s'.split()
if __name__=="__main__":
    print "Permutations of ", ts
    #for p in xpermutations(ts): print ''.join(p)

    print "Combinations of ", ts
    #for c in xcombinations(ts,2): print ''.join(c)

    print "Unique Combinations of ", ts
    for uc in xuniqueCombinations(ts,8): print ''.join(uc)

    print "Selections of 2 ", ts
    #for s in xselections(ts,2): print ''.join(s)
    #print map(''.join, list(xpermutations('done')))
