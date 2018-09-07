fin = open('relativity1.txt', 'rt' )
poem = fin.read()
fin.close()
print(poem)

poem = ''
fin = open('relativity1.txt', 'rt' )
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(poem)

poem = ''
fin = open('relativity1.txt', 'rt' )
for line in fin:
    poem += line

fin.close()
print(poem)

fin = open('relativity1.txt', 'rt' )
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')

for line in lines:
    print(line)

for line in lines:
    print(line, end='')

