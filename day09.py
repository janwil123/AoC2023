from itertools import pairwise

# Read and parse the input

with open("input09.txt") as f:
    lines = f.read().splitlines()

numlines = []

for line in lines:
    numlines.append(list(map(int,line.split())))

# Parts 1&2

def diff(l):
    return([y-x for (x, y) in pairwise(l)])

def allzero(l):
    return(sum(list(map(lambda x: x*x,l)))==0)

S = 0
T = 0

for nl in numlines:
    s = 0
    t = 0
    d = 1
    while not(allzero(nl)):
        s += nl[-1]
        t += d*nl[0]
        d *= -1
        nl = diff(nl)
    S += s
    T += t

print(S)
print(T)

