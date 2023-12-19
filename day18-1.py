from sys import setrecursionlimit
setrecursionlimit(50000)

# Read and parse the input

with open("input18.txt") as f:
    lines = f.read().splitlines()

dirs = []
lens = []
cols = []

for line in lines:
    d,l,c = line.split()
    dirs.append(d)
    lens.append(int(l))
    cols.append(c[2:-1])

# Part 1

holes = [(0,0)]

for i in range(len(dirs)):
    match dirs[i]:
        case 'R':
            for j in range(lens[i]):
                h = holes[-1]
                holes.append((h[0]+1,h[1]))
        case 'L':
            for j in range(lens[i]):
                h = holes[-1]
                holes.append((h[0]-1,h[1]))
        case 'D':
            for j in range(lens[i]):
                h = holes[-1]
                holes.append((h[0],h[1]+1))
        case 'U':
            for j in range(lens[i]):
                h = holes[-1]
                holes.append((h[0],h[1]-1))     

# Find the bounding box

minx = 1000
miny = 1000
maxx = 0
maxy = 0

for h in holes:
    if h[0] < minx:
        minx = h[0]
    if h[1] < miny:
        miny = h[1]        
    if h[0] > maxx:
        maxx = h[0]
    if h[1] > maxy:
        maxy = h[1] 

lx = maxx - minx + 1
ly = maxy - miny + 1

M = [['.' for _ in range(lx)] for _ in range(ly)]

for h in holes:
    M[h[1]-miny][h[0]-minx] = '#'

# Upper left corner
    
startx = ''.join(M[0]).find('#') + 1
starty = 1

visited = set()

def dfs(v):
    x,y = v
    if not(v in visited) and not(M[y][x]=='#'):
        visited.add(v)
        dfs((x+1,y))
        dfs((x-1,y))
        dfs((x,y+1))
        dfs((x,y-1))

dfs((startx,starty))

print(len(holes)-1+len(visited))