from copy import deepcopy

# Read and parse the input

with open("input13.txt") as f:
    lines = f.read().splitlines()
    lines.append('')

Matrices = []
M = []

for l in lines:
    if l == '':
        Matrices.append(M)
        M = []
    else:
        M.append(list(l))

# Part 1

def findrowreflection(M):
    n = len(M)
    for i in range (1,n):
        is_reflection = True
        for j in range(min(i,n-i)):
            if M[i+j] != M[i-1-j]:
                is_reflection = False
                break
        if is_reflection:
            return(i)
    return(0)

s = 0
reflections = []

for M in Matrices:
    r = findrowreflection(M)
    if r != 0:
        s += 100*r
        reflections.append(('r',r))
    else: 
        t = findrowreflection(list(zip(*M)))
        s += t
        reflections.append(('c',t))

print(s)

# Part 2

def findrowreflection2(M,r):
    n = len(M)
    for i in range (1,n):
        is_reflection = True
        for j in range(min(i,n-i)):
            if M[i+j] != M[i-1-j]:
                is_reflection = False
                break
        if is_reflection and (i != r):
            return(i)
    return(0)

s = 0

for k in range(len(Matrices)):
    # Look for reflection in rows
    M = Matrices[k]
    is_reflection = False
    for j in range(len(M)):
        for i in range(len(M[0])):
            Mc = deepcopy(M)
            if Mc[j][i] == '.':
                Mc[j][i] = '#'
            else:
                Mc[j][i] = '.'
            if 'r'==reflections[k][0]:
                r = findrowreflection2(Mc,reflections[k][1])
            else:
                r = findrowreflection(Mc)
            if r != 0:
                is_reflection = True
                s += 100*r
                break
        if is_reflection:
            break
    if is_reflection:
        continue
    # No row reflection, transpose the matrix
    M = list(map(lambda x:list(x),list(zip(*M))))
    is_reflection = False
    for j in range(len(M)):
        for i in range(len(M[0])):
            Mc = deepcopy(M)
            if Mc[j][i] == '.':
                Mc[j][i] = '#'
            else:
                Mc[j][i] = '.'
            if 'c'==reflections[k][0]:
                r = findrowreflection2(Mc,reflections[k][1])
            else:
                r = findrowreflection(Mc)
            if r != 0:
                is_reflection = True
                s += r
                break
        if is_reflection:
            break    

print(s)