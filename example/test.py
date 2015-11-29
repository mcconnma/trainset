from ctypes import *

c = cdll.LoadLibrary("./libdoit.so")
print('retval: ', c.doit())
