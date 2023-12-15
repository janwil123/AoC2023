from copy import deepcopy

# Read and parse the input

with open("input14.txt") as f:
    Matrix = list(map(list,f.read().splitlines()))

n = len(Matrix) # We have an nxn square

# Part 1

def tiltN(M):
    for i in range(n):
        row = 0
        for j in range(n):
            match M[j][i]:
                case 'O':
                    M[j][i] = '.'
                    M[row][i] = 'O'
                    row += 1
                case '#':
                    row = j+1
    return(M)

def countmat(M):
    res = 0
    for j in range(n):
        for i in range(n):
            if M[j][i] == 'O':
                res += (n-j)
    return(res)

M = deepcopy(Matrix)

print(countmat(tiltN(M)))

# Part 2

def tiltE(M):
    for j in range(n):
        col = n-1
        for i in range(n-1,-1,-1):
            match M[j][i]:
                case 'O':
                    M[j][i] = '.'
                    M[j][col] = 'O'
                    col -= 1
                case '#':
                    col = i-1            
    return(M)

def tiltS(M):
    for i in range(n):
        row = n-1
        for j in range(n-1,-1,-1):
            match M[j][i]:
                case 'O':
                    M[j][i] = '.'
                    M[row][i] = 'O'
                    row -= 1
                case '#':
                    row = j-1
    return(M)

def tiltW(M):
    for j in range(n):
        col = 0
        for i in range(n):
            match M[j][i]:
                case 'O':
                    M[j][i] = '.'
                    M[j][col] = 'O'
                    col += 1
                case '#':
                    col = i+1            
    return(M)

def cycle(M):
    return(tiltE(tiltS(tiltW(tiltN(M)))))

def cyclemat(Mat,num):
    M = deepcopy(Mat)
    for _ in range(num):
        M = cycle(M)
    return(M)

M = deepcopy(Matrix)
matrices = []
i = 0

while True:
    i += 1
    M = cycle(M)
    if M in matrices:
        second = i
        first = matrices.index(M)+1
        break
    else:
        M1 = deepcopy(M)
        matrices.append(M1)


d = second - first
k = 1000000000-d*(1000000000//d)

M = deepcopy(Matrix)

print(countmat(cyclemat(M,k+d*(1+first//d))))