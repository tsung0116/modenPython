# [ EXPRESSION for Sign in List if CONDITION]

list1 = [ x * 2 for x in range(0,5)]
print(list1)

list2 = [ x for x in range(0,10) if x % 2 == 0]
print(list2)

c=[(1,2),(3,4),(5,6)]
list3 = [ i for i,j in c] 
print(list3)

list4 = [[i*2, j*3, i+j] for i,j in c]
print(list4)
