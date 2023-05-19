from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine
 
print(machine())

from platform import processor
 
print(processor())

from platform import system
 
print(system())
from platform import version
 
print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

    import math
    a=math.e
    print(a)
    b=math.exp(1)
    print(b)
    zeroes = [0 for i in range(5)]
    print(zeroes)

import sys
 
for p in sys.path:
  print(p)
  print('..\\modules')