from queue import PriorityQueue

# Read and parse the input

with open("input17.txt") as f:
    lines = f.read().splitlines()

M = []
for l in lines:
    M.append(list(map(int,list(l))))

n = len(M) # We have nxn matrix

infty = 1000000

# Part 1

minlen = 1
maxlen = 3

# Uncomment this for Part 2

# minlen = 4
# maxlen = 10

# Form a graph

V = [((0,0),(0,0),0)]

for j in range(n):
    for i in range(n-1):
        for k in range(i+minlen,min(i+maxlen+1,n)):
            V.append(((i,j),(k,j),sum(M[j][i+1:k+1])))
            V.append(((k,j),(i,j),sum(M[j][i:k])))
                     
Mt = list(zip(*M))

for j in range(n):
    for i in range(n-1):
        for k in range(i+minlen,min(i+maxlen+1,n)):
            V.append(((j,i),(j,k),sum(Mt[j][i+1:k+1])))
            V.append(((j,k),(j,i),sum(Mt[j][i:k])))

V.append(((n-1,n-1),(n-1,n),0))
V.append(((n-1,n-1),(n,n-1),0))

def dir(v):
    s,t,d = v 
    if s[0] < t[0]:
        return('hor')
    if s[0] > t[0]:
        return('hor')
    if s[1] < t[1]:
        return('ver')
    if s[1] > t[1]:
        return('ver')        
    
def neighbours(v):
    if v == ((0,0),(0,0),0):
        res = []
        for x in range(minlen,maxlen+1):
            res.append(((0,0),(x,0),sum(M[0][1:x+1])))
        for y in range(minlen,maxlen+1):
            res.append(((0,0),(0,y),sum(Mt[0][1:y+1])))        
    else: 
        s,t,d = v
        if t == (n-1,n-1):
            if dir(v) == 'hor':
                res = [((n-1,n-1),(n-1,n),0)]
            else:
                res = [((n-1,n-1),(n,n-1),0)]
        else:
            res = []
            if dir(v) == 'hor':
                x = t[0]
                for y in range(t[1]+minlen,min(t[1]+maxlen+1,n)):
                    summa = sum(Mt[x][t[1]+1:y+1])
                    res.append((t,(x,y),summa))
                for y in range(t[1]-minlen,max(t[1]-(maxlen+1),-1),-1):
                    summa = sum(Mt[x][y:t[1]])
                    res.append((t,(x,y),summa))
            else: # dir(v) = 'ver'
                y = t[1]
                for x in range(t[0]+minlen,min(t[0]+maxlen+1,n)):
                    summa = sum(M[y][t[0]+1:x+1])
                    res.append((t,(x,y),summa))
                for x in range(t[0]-minlen,max(t[0]-(maxlen+1),-1),-1):
                    summa = sum(M[y][x:t[0]])
                    res.append((t,(x,y),summa)) 
    return(res)          


q = PriorityQueue()

q.put((0,((0,0),(0,0),0)))

dist = {}

dist[((0,0),(0,0),0)] = 0 

for v in V[1:]:
    dist[v] = infty

black = set()

while not q.empty():
    node = q.get()
    if not (node[1] in black):
        black.add(node[1])
        if node[1] in [((n-1,n-1),(n-1,n),0),((n-1,n-1),(n,n-1),0)]:
            print(f'Minimal distance is {dist[node[1]]}')
            break
        s,t,d = node[1]
        for v in neighbours(node[1]):
            alt = dist[node[1]] + v[2]
            if alt < dist[v]:
                dist[v] = alt
                q.put((alt,v))



        

