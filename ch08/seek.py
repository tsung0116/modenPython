# read the last byte in different ways

fin = open('bfile1', 'rb')
print(fin.tell())

# 1. Absolute location
fin.seek(255)

bdata = fin.read()
print(len(bdata))
print(bdata[0])


fin.seek(0)
print(fin.tell())

# 2. One byte before the end of the file
fin.seek(-1, 2)         
print(fin.tell())

bdata = fin.read()     
print(len(bdata))
print(bdata[0])

# 3. Current location
fin.seek(254, 0)
fin.seek(1, 1)         
print(fin.tell())

bdata = fin.read()     
print(len(bdata))
print(bdata[0])
