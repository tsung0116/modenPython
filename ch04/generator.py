range1 = range(1,10)
print(type(range1))
print(sum(range1))

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)

ranger = my_range(1, 5)
print(ranger)
print(sum(ranger))
for x in ranger:
    print(x)

