bdata = bytes(range(0, 256))

fout = open('bfile1', 'wb')
fout.write(bdata)

fout.close()

fout = open('bfile2', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fin = open('bfile1', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

