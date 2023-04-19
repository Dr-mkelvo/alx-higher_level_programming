#!/usr/bin/python3
from attribute_tests import A
x = A()
print(x.pub)
x.pub = x.pub + " My value can be changed"
print(x.pub)
print(x._prot)
#x.prot = x.prot + "Protected from Change"
#print(x.priv)