import csv

villains = [['Doctor', 'No'],['Rosa', 'Klebb'],['Mister', 'Big'],['Auric', 'Goldfinger'],['Ernst', 'Blofeld'],]
print(villains)

#  On Windows, CSV.writer() adds an extra carriage return (\r), if newline='' is not specified. 
with open('villains1.csv', 'wt', newline='') as fout: # a context manager
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains1.csv', 'rt', newline='') as fin: # context manager
    cin = csv.reader(fin)
    villains = [row for row in cin] # This uses a list comprehension

print(villains)

with open('villains1.csv', 'rt', newline='') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

with open('villains2.csv', 'wt', newline='') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)


with open('villains2.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)