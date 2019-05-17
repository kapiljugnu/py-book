import sys

# tuples are immutable

data = (1, 2, 9) # literal
data2 = tuple() # constructor

print(data)
print(data2)

data3 = (5,6,10)

strTuple = ('A', 'B')
strTuple2 = ('C', 'D')

print(data < data3) # => True, compare each element in tuple, 1 with 5, 2 with 6 and 9 with 10
print( strTuple > strTuple2) # => False

try:
    a,b,c,d = data

    print(a,b,c,d)
except :
    print('error')


di = {  'c': 30, 'a': 10, 'b': 20 }
sortVal = sorted([(v,k) for k,v in di.items()]) # list comprehension
print(sortVal)