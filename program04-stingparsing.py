s = 'hello'
print(list(s))

name = ' Timmy Hsu'
first, last = name.split()
print("{} + {}".format(first, last))

print("/path/to/a/folder".split('/'))

import os
print(os.environ['PATH'].split(os.pathsep))

print("Apple,Bananas,Chips,Bread,Fish".split(','))

print('Apple and Bananas'.split(' and '))

print("Apple,Bananas,Chips,Bread,Fish".split(',',2))

file_path = '/some/path/to/some_file.ext'
print(file_path.split('.',1)[-1])
print(file_path.split('/',1)[-1])
print(file_path.split('/',1)[0])
print(file_path.split('/',4)[-1])

parts = 'Apple and Bananas'.split(' and ')
print(' or '.join(parts))