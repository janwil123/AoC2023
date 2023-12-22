import numpy as np

# Read and parse the input

with open("input21.txt") as f:
    lines = f.read().splitlines()

t = 5 

n = t*len(lines)+2 # We will have an nxn matrix with a frame of #-s

M = ['#'*n]
for _ in range(t):
    for l in lines:
        M.append('#'+l*t+'#')
M.append('#'*n)

# S is in the middle

sx = n//2
sy = n//2

# Part 2
    
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    
def step(inset):
    outset = set()
    for x,y in inset:
        for dx,dy in dirs:
            if M[y+dy][x+dx] != '#':
                outset.add((x+dx,y+dy))
    return(outset)

S = set([(sx,sy)])

# We need to find values for t=1,3,5 by force, and can then
# solve a linear system of equations for three variables 
# expressing numbers of '#'-s in different repeating blocks.

steps = 65

stepres = []

for _ in range(steps):
    S = step(S)
stepres.append((1,len(S)))

for i in range(1,t//2+1):
    for _ in range(2*65+1):
        S = step(S)
    stepres.append((2*i+1,len(S)))

Mat = []
Vec = []

for st in stepres:
    t,e = st
    s = 65*t+t//2
    a = t//2+1
    b = t//2
    Mat.append([a**2,b**2,a*b])
    Vec.append((s+1)**2-e)

A = np.array(Mat)
B = np.array(Vec)
X = np.linalg.solve(A,B)

x0 = round(X[0])
x1 = round(X[1])
x2 = round(X[2])

def comp(t):
    s = 65*t+t//2
    a = t//2+1
    b = t//2
    return((s+1)**2-a**2*x0-b**2*x1-a*b*x2)

# 26501365 = 65*t + t//2, where t=404601.

print(comp(404601)) 