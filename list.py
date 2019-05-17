# list are mutable

data = list() # constructor
data2 = [] # literal

for i in range(5) :
    data.append(i+1)
    data2.append(i+2)

print(data) # => [1, 2, 3, 4, 5]
print(data[:]) # same as print(data), can be use to copy list , => [1, 2, 3, 4, 5]
print(data2) # => [2, 3, 4, 5, 6]
print(data[:2]) # start to index 1, not including index 2, => [1, 2]
print(data2[2:]) # begin with index 2 and include rest, => [4, 5, 6]
