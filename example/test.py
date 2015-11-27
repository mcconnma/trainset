from ctypes import *

#cdll.LoadLibrary("libc.so.6")
#libc = CDLL("libc.so.6")
#libc.printf(b'hello %s', b'mark\n')

c = CDLL("./libdoit.so")
print('retval: ', c.doit())
