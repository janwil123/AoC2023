# Read and parse the input

with open("input21.txt") as f:
    lines = f.read().splitlines()

n = len(lines)+2 # We will have an nxn matrix with a frame of #-s

M = ['#'*n]
for l in lines:
    M.append('#'+l+'#')
M.append('#'*n)

# Find the coordinates of S

for sy in range(n):
    sx = M[sy].find('S')
    if sx >= 0:
        break

# Part 1
    
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    
def step(inset):
    outset = set()
    for x,y in inset:
        for dx,dy in dirs:
            if M[y+dy][x+dx] != '#':
                outset.add((x+dx,y+dy))
    return(outset)

S = set([(sx,sy)])

for _ in range(64):
    S = step(S)

print(len(S))

# Part 2

# 26501365 = 65*t + t//2, where t=404601. The geometrical shape where the Elf is able to get to
# forms a perfect rhombus. You can compute the number of potential end plots as 26501366**2, and then you have
# to subtract the plots with '#'-s. These also appear regularly in smaller rhombi. You can count the number
# of '#'-s in the 8 triangles of the original map and take it from there. I computed the '#'-s in the rhombi
# by finding the exact number of 'O'-s for small values of t, forming a system of 3 linear equations and 
# solving it. This is where the magical constants 488, 463 and 1013 appear from.

def comp(t):
    s = 65*t+t//2
    a = t//2+1
    b = t//2
    return((s+1)**2-a**2*488-b**2*463-a*b*1013)

print(comp(404601)) 