from collections import defaultdict

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
        if M[y][x+1] == '>':
            E[v].append(walk((x,y),(x+1,y)))
        if M[y][x-1] == '<':
            E[v].append(walk((x,y),(x-1,y)))
        if M[y+1][x] == 'v':
            E[v].append(walk((x,y),(x,y+1)))
        if M[y-1][x] == '^':
            E[v].append(walk((x,y),(x,y-1)))

def traverse(u):
    if u == (n-2,n-1):
        return([[]])
    else:
        res = []
        for (v,path) in E[u]:
            for p in traverse(v):
                res.append(path+p)
        return(res)

paths = traverse((1,0))
m = 0
for p in paths:
    if m < len(p):
        m = len(p)
print(m)
