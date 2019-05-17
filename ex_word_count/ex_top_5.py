fname = input('Enter File:')
if len(fname) < 1 : 
    fname = 'clown.txt'

hand = open(fname);

di = dict()

for line in hand :
    line = line.rstrip()
    wds = line.split()
    for w in wds :
        di[w] = di.get(w, 0) + 1

# top 5 used words

valueFirst = [(v,k) for k,v in di.items()]
sortedValue = sorted(valueFirst, reverse=True)

print(sortedValue[:5])