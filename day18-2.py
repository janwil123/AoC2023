from collections import defaultdict

# Read and parse the input

with open("input18.txt") as f:
    lines = f.read().splitlines()

dirs = []
lens = []

for line in lines:
    _,_,l = line.split()
    match l[-2]: 
        case '0':
            dirs.append('R')
        case '1':
            dirs.append('D')
        case '2':
            dirs.append('L')
        case '3':
            dirs.append('U')
    lens.append(int(l[2:-2],16))

# Part 2

colcorners = defaultdict(list) # Lists corners for each column where there are corners
colcorners[0].append(0)
cornerdirs = {} # The direction (NW,SW,SE,NE) each corner is facing
cornerdirs[(0,0)] = 'NW'
cornercols = set([0]) # Lists columns where there are corners

cx = 0
cy = 0

for i in range(len(dirs)-1):
    match dirs[i]:
        case 'R':
            cx += lens[i]
        case 'L':
            cx -= lens[i]
        case 'D':
            cy += lens[i]
        case 'U':
            cy -= lens[i]
    colcorners[cx].append(cy)
    cornercols.add(cx)
    match dirs[i]+dirs[i+1]:
        case 'RD':
            cornerdirs[(cx,cy)]='NE'
        case 'UL':
            cornerdirs[(cx,cy)]='NE'        
        case 'LD':
            cornerdirs[(cx,cy)]='NW'
        case 'UR':
            cornerdirs[(cx,cy)]='NW'
        case 'RU':
            cornerdirs[(cx,cy)]='SE'
        case 'DL':
            cornerdirs[(cx,cy)]='SE'
        case 'LU':
            cornerdirs[(cx,cy)]='SW'
        case 'DR':
            cornerdirs[(cx,cy)]='SW'      
            
for k in colcorners:
    colcorners[k].sort()

cornercols = sorted(list(cornercols))

lastx = cornercols[0]
ys = colcorners[lastx]
currentrows = ys
S = 0
for j in range(len(ys)//2):
    S += (ys[2*j+1]-ys[2*j]+1)

for x in cornercols[1:]:
    for j in range(len(currentrows)//2):
        S += (x-lastx-1)*(currentrows[2*j+1]-currentrows[2*j]+1)
    colsum = 0
    criticalrows = sorted(list(set(currentrows).union(set(colcorners[x]))))
    mode = 'outside'
    for y in criticalrows:
        match mode:
            case 'outside':
                if not(y in colcorners[x]):
                    lasty = y
                    mode = 'inside'
                else: # We are in a corner
                    lasty = y
                    if cornerdirs[(x,y)] == 'NW':
                        mode = 'edge-out-left'
                    elif cornerdirs[(x,y)] == 'NE':
                        mode = 'edge-out-right'
                    else:
                        print("We should never reach here 1")
            case 'inside':
                if not(y in colcorners[x]):
                    colsum += (y-lasty+1)
                    mode = 'outside'
                else:  # We are in a corner
                    if cornerdirs[(x,y)] == 'NW':
                        mode = 'edge-out-right'
                    elif cornerdirs[(x,y)] == 'NE':
                        mode = 'edge-out-left'
                    else:
                        print("We should never reach here 2")
            case 'edge-out-left':
                if y in colcorners[x]:
                    if cornerdirs[(x,y)] == 'SE':
                        mode = 'inside'
                    elif cornerdirs[(x,y)] == 'SW':
                        mode = 'outside'
                        colsum += (y-lasty+1)
                    else:
                        print("We should never reach here 3")
                else:
                    print("We should never reach here 4")
            case 'edge-out-right':
                if y in colcorners[x]:
                    if cornerdirs[(x,y)] == 'SW':
                        mode = 'inside'
                    elif cornerdirs[(x,y)] == 'SE':
                        mode = 'outside'
                        colsum += (y-lasty+1)
                    else:
                        print("We should never reach here 5")
                else:
                    print("We should never reach here 6")                
    S += colsum

    lastx = x
    newrows = []
    for j in criticalrows:
        if j in currentrows and not(j in colcorners[x]):
            newrows.append(j)
        if not(j in currentrows) and j in colcorners[x]:
            newrows.append(j)

    currentrows = newrows

print(S)