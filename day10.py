# Read and parse the input

with open("input10.txt") as f:
    M = f.read().splitlines()

n = len(M) # We have an nxn square

# Find coordinates of S

for yS in range(n):
    xS = M[yS].find('S')
    if xS >= 0:
        break

# Part 1

dirs = {('|',0,1):(0,1),('|',0,-1):(0,-1),('-',1,0):(1,0),('-',-1,0):(-1,0),
        ('L',0,1):(1,0),('L',-1,0):(0,-1),('J',0,1):(-1,0),('J',1,0):(0,-1),
        ('7',1,0):(0,1),('7',0,-1):(-1,0),('F',0,-1):(1,0),('F',-1,0):(0,1)}

N = [['.' for _ in range(n)] for _ in range(n)] # This matrix is required for Part 2. 
                                                # It is M with junk removed.

l = 1
dx,dy = 0,1 # The first pipe is below S
N[yS][xS] = 'F' # In all my examples, 'F' fits for S
x,y = xS+dx,yS+dy
while (x,y) != (xS,yS):
    N[y][x] = M[y][x]
    (dx,dy) = dirs[(M[y][x],dx,dy)]
    x,y = x+dx,y+dy
    l+=1

print(l//2)

# Part 2

incnt = 0

for y in range(n):
    for x in range(n):
        if N[y][x] == '.':
            crossings = 0
            i = x
            mode = '.'
            while i < n:
                match N[y][i]:
                    case '|':
                        crossings += 1
                    case 'F':
                        mode = 'F'
                    case 'J':
                        if mode == 'F':
                            crossings += 1
                            mode = '.'
                        elif mode == 'L':
                            mode = '.'
                    case 'L':
                        mode = 'L'
                    case '7':
                        if mode == 'F':
                            mode = '.'
                        elif mode == 'L':
                            crossings += 1
                            mode = '.'                        
                i += 1
            incnt += (crossings%2)

print(incnt)