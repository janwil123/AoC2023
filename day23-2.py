from copy import deepcopy
from collections import defaultdict
from random import randint

# Read and parse the input

with open("input23.txt") as f:
    M = f.read().splitlines()

n = len(M) # We have an nxn square

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

V = [(1,0)]

for j in range(1,n-1):
    for i in range(1,n-1):
        c = 0
        for d in dirs:
            dx,dy = d
            if M[j+dy][i+dx] in ['^','>','v','<']:
                c+=1
        if c >= 3:
            V.append((i,j))

V.append((n-2,n-1))

E = defaultdict(list)

def walk(a,b):
    prev = a
    curr = b
    path = []
    while not(curr in V):
        path.append(curr)
        x,y = curr
        for d in dirs:
            dx,dy = d
            nextfound = False
            if (M[y+dy][x+dx] != '#') and ((x+dx,y+dy) != prev):
                prev = curr
                curr = (x+dx,y+dy)
                nextfound = True
            if nextfound:
                break
    path.append(curr)
    return(curr,path)

for v in V[:-1]:
    if v == (1,0):
        E[v].append(walk((1,0),(1,1)))
    else:
        x,y = v
        for d in dirs:
            dx,dy = d
            if M[y+dy][x+dx] != '#':
                E[v].append(walk((x,y),(x+dx,y+dy)))

G = defaultdict(set)
for u in V:
    for (v,path) in E[u]:
        G[u].add(v)
        G[v].add(u)

def rndpath(p):
    u = p[-1]
    if u == (n-2,n-1):
        return(p)
    nxt = []
    for v in G[u]:
        if not(v in p):
            nxt.append(v)
    if len(nxt) == 0:
        j = randint(1,len(p))
        return(rndpath(p[:j]))
    else:
        i = randint(0,len(nxt)-1)
        return(rndpath(p+[nxt[i]]))

m = 0
while True: # Wait until numbers get no more larger
    path = rndpath([(1,0)])
    s = 0
    for i in range(len(path)-1):
        u = path[i]
        v = path[i+1]
        for (a,p) in E[u]:
            if a == v:
                s += len(p)
    if s > m:
        m = s
        print(m)

    
