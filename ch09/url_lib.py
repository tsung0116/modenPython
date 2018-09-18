import urllib.request as ur

url = 'http://192.168.1.17'
conn = ur.urlopen(url)
print(conn)

data = conn.read()
print(data)

print(conn.status)
print(conn.getheader('Content-Type'))

for key, value in conn.getheaders():
    print(key, value)