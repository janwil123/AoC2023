# Read and parse the input

with open("input16.txt") as f:
    M = f.read().splitlines()

n = len(M) # nxn square

# Part 1

def process(start):
    energized = set()
    to_process = [start]
    processed = set()

    while len(to_process) > 0:
        tp = to_process[-1]
        x,y,d = tp
        tile = M[y][x]
        match tile:
            case '.':
                match d:
                    case 'l':
                        nxt = [(x+1,y,'l')]
                    case 'r':
                        nxt = [(x-1,y,'r')]
                    case 'u':
                        nxt = [(x,y+1,'u')]
                    case 'd':
                        nxt = [(x,y-1,'d')]
            case '/':
                match d:
                    case 'l':
                        nxt = [(x,y-1,'d')]
                    case 'r':
                        nxt = [(x,y+1,'u')]
                    case 'u':
                        nxt = [(x-1,y,'r')]
                    case 'd':
                        nxt = [(x+1,y,'l')]           
            case '\\':
                match d:
                    case 'l':
                        nxt = [(x,y+1,'u')]
                    case 'r':
                        nxt = [(x,y-1,'d')]
                    case 'u':
                        nxt = [(x+1,y,'l')]
                    case 'd':
                        nxt = [(x-1,y,'r')]  
            case '|':
                match d:
                    case 'l':
                        nxt = [(x,y+1,'u'),(x,y-1,'d')]
                    case 'r':
                        nxt = [(x,y+1,'u'),(x,y-1,'d')]
                    case 'u':
                        nxt = [(x,y+1,'u')]
                    case 'd':
                        nxt = [(x,y-1,'d')]             
            case '-':
                match d:
                    case 'l':
                        nxt = [(x+1,y,'l')]
                    case 'r':
                        nxt = [(x-1,y,'r')]
                    case 'u':
                        nxt = [(x-1,y,'r'),(x+1,y,'l')]
                    case 'd':
                        nxt = [(x-1,y,'r'),(x+1,y,'l')] 
        energized.add((x,y))
        to_process = to_process[:-1]
        processed.add(tp)
        for step in nxt:
            sx,sy,sd = step
            if (0 <= sx < n) and (0 <= sy < n):
                if not(step in processed):
                    to_process.append(step)

    return(len(energized))

print(process((0,0,'l')))

# Part 2

mm = 0
for i in range(n):
    nn = process((i,0,'u'))
    if nn > mm:
        mm = nn
for i in range(n):
    nn = process((i,n-1,'d'))
    if nn > mm:
        mm = nn
for i in range(n):
    nn = process((0,i,'l'))
    if nn > mm:
        mm = nn
for i in range(n):
    nn = process((n-1,i,'r'))
    if nn > mm:
        mm = nn

print(mm)