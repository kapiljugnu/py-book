
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
    # Traceback (most recent call last):
    # File "tuples.py", line 19, in <module>
    # a,b,c,d = data
    # ValueError: not enough values to unpack (expected 4, got 3)
    a,b,c,d = data 

    print(a,b,c,d)
except :
    pass


try:
    # Traceback (most recent call last):
    #File "tuples.py", line 32, in <module>
    # data[0] = 10
    # TypeError: 'tuple' object does not support item assignment
    data[0] = 10
except:
    pass