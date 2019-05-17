 
purse = dict() # constructor
anotherPurse = { 'money': 200, 'candy': 5} # literal

purse['money'] = 100
purse['candy'] = 2

print(purse) # => {'money': 100, 'candy': 2}

print(purse['candy']) # => 2

print(anotherPurse) # => {'money': 200, 'candy': 5}

print('money' in anotherPurse) # => True
print(anotherPurse.get('money1', 0)) # => 0

print('xyz' in purse) # => False

print(list(purse)) # => ['money', 'candy']
print(purse.keys()) # => dict_keys(['money', 'candy'])
print(purse.values()) # => dict_values([100, 2])
print(purse.items()) # => dict_items([('money', 100), ('candy', 2)])

for key, value in purse.items():
    print(key, value)