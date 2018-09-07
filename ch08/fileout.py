poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

lines1 = ["One", "Two", "Three", "Four", "Five"]
lines2 = ["One\n", "Two\n", "Three\n", "Four\n", "Five\n"]

fout = open('relativity1.txt', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity2.txt', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity3.txt', 'wt')
print(lines1, file=fout)
fout.close()

fout = open('relativity3.txt', 'a')
print(lines1, 'hello', file=fout, sep='%%', end='$$$')
fout.close()

fout = open('relativity3.txt', 'a')
print(lines2, file=fout)
fout.close()

fout = open('relativity4.txt', 'wt')
fout.writelines(lines1)
fout.close()

fout = open('relativity4.txt', 'a')
fout.writelines(lines2)
fout.close()

fout = open('relativity5.txt', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk

fout.close()

with open('relativity6.txt', 'wt') as fout:
    print(poem, file=fout, sep='', end='')
