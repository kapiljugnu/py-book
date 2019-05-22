import re

str = "welcome to :) the python book :)"

print(len(str))

# match the 'book' term in the string
result = re.search('book', str) # => <re.Match object; span=(22, 26), match='book'>
print(result)

# match the string if it start with 'o' character
result = re.search('^o', str) # => None
print(result)

# match the string which start with character 'w' and contain 0 or more character after it
# and contain ':)' character
# this will match both the ':)' term in the string, at position 12 and 32.
# because of its greedy nature, largest of the 2 string
result = re.search('^w.* :\)', str)
print(result)

# same as above but restrict the greedy nature by using the '?' after the '*'
result = re.search('^w.*? :\)', str) 
print(result)
