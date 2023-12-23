from collections import defaultdict
from copy import deepcopy

# Read and parse the input

with open("input22.txt") as f:
    lines = f.read().splitlines()

bricks = []

maxx = 9
maxy = 9
maxz = 339

M = [[[-1 for _  in range(maxx+1)] for _ in range(maxy+1)] for _ in range(maxz+1)]

for i in range(len(lines)):
    l = lines[i]
    a,b = l.split('~')
    x1,y1,z1 = map(int,a.split(','))
    x2,y2,z2 = map(int,b.split(','))
    bricks.append([[x1,y1,z1],[x2,y2,z2]])
    if x1 < x2 and y1 == y2 and z1 == z2:
        for j in range(x1,x2+1):
            M[z1][y1][j] = i
    elif x1 == x2 and y1 < y2 and z1 == z2:
        for j in range(y1,y2+1):
            M[z1][j][x1] = i
    elif x1 == x2 and y1 == y2:
        for j in range(z1,z2+1):
            M[j][y1][x1] = i

# Part 1
        
def fall(): # Attempts to fall a brick and returns its number if successful
    for i in range(len(bricks)):
        brick = bricks[i]
        x1,y1,z1 = brick[0]
        x2,y2,z2 = brick[1]
        canfall = False
        if z1>1 and z2>1:
            if x1 < x2 and y1 == y2 and z1 == z2:
                belowempty = True
                for j in range(x1,x2+1):
                    if M[z1-1][y1][j] != -1:
                        belowempty = False
                        break
                if belowempty:
                    canfall = True
                    bricks[i] = [[x1,y1,z1-1],[x2,y2,z2-1]]
                    for j in range(x1,x2+1):
                        M[z1][y1][j] = -1
                        M[z1-1][y1][j] = i        
                
            elif x1 == x2 and y1 < y2 and z1 == z2:
                belowempty = True
                for j in range(y1,y2+1):
                    if M[z1-1][j][x1] != -1:
                        belowempty = False
                        break
                if belowempty:
                    canfall = True
                    bricks[i] = [[x1,y1,z1-1],[x2,y2,z2-1]]
                    for j in range(y1,y2+1):
                        M[z1][j][x1] = -1
                        M[z1-1][j][x1] = i 
            elif x1 == x2 and y1 == y2:
                if M[z1-1][y1][x1] == -1:
                    canfall = True
                    bricks[i] = [[x1,y1,z1-1],[x2,y2,z2-1]]
                    for j in range(z1,z2+1):
                        M[j-1][y1][x1] = i
                    M[z2][y1][x1] = -1
        
        if canfall:
            return(i)
    return(-1)
                                
while True:
    didfall = fall()
    if didfall == -1:
        break

support = defaultdict(set)

for i in range(len(bricks)):
    brick = bricks[i]
    x1,y1,z1 = brick[0]
    x2,y2,z2 = brick[1]
    if x1 < x2 and y1 == y2 and z1 == z2:
        for j in range(x1,x2+1):
            if M[z1-1][y1][j] != -1:
                support[i].add(M[z1-1][y1][j])
    elif x1 == x2 and y1 < y2 and z1 == z2:
        for j in range(y1,y2+1):
            if M[z1-1][j][x1] != -1:
                support[i].add(M[z1-1][j][x1])
    elif x1 == x2 and y1 == y2:
        if M[z1-1][y1][x1] != -1:
            support[i].add(M[z1-1][y1][x1])

nonsafe = set()

for i in range(len(bricks)):
    s = support[i]
    if len(s) == 1:
        nonsafe.add(list(s)[0])

print(len(bricks)-len(nonsafe))

# Part 2

ln = list(nonsafe)

bricksc = deepcopy(bricks)
Mc = deepcopy(M)
fallen = []

for i in range(len(ln)):
    br = ln[i]
    bricks = deepcopy(bricksc)
    bricks = bricks[:br]+bricks[(br+1):]
    M = deepcopy(Mc)
    for z in range(maxz+1):
        for y in range(maxy+1):
            for x in range(maxx+1):
                if M[z][y][x] == br:
                    M[z][y][x] = -1
                if M[z][y][x] > br:
                    M[z][y][x] -= 1
    fallset = set()
    while True:
        didfall = fall()
        if didfall == -1:
            break
        else:
            fallset.add(didfall)
    fallen.append(len(fallset))

print(sum(fallen))

