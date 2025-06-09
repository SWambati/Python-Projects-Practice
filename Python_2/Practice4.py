#this program tests out the platform module

from platform import platform
from platform import machine
from platform import processor
from platform import system, version, python_implementation, python_version_tuple

result1 = platform()
result2 = platform(1)
result3 = platform(1, 1)
result4 = platform(0, 1)
result5 = platform(0, 0)

result6 = machine()

result7 = processor()

result8 = system()

result9 = version()

result10 = python_implementation()

result11 = python_version_tuple()

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)