# Read and parse the input

with open("input03.txt") as f:
    lines = f.read().splitlines()

n = len(lines) # The input is an nxn square

# Put a dotted frame around

scheme = ['.'*(n+2)]
for line in lines:
    scheme.append('.'+line+'.')
scheme.append('.'*(n+2))

# Find the positions where there are numbers

numpositions = []

for j in range(1,n+1):
    s = scheme[j]
    i = 1
    numactive = False # Whether we are currently parsing a number or not
    while i < n+2:
        if s[i] in '0123456789':
            if not(numactive):
                l = i 
                numactive = True
        else: # s[i] is not a number
            if numactive:
                numpositions.append((j,l,i-1))
                numactive = False
        i += 1

# Part 1

# Return a number on that position

def compnum(pos):
    (j,l,r) = pos
    n = 0
    for i in range(l,r+1):
        n *= 10
        n += int(scheme[j][i])
    return(n)

partnumbers = []

for np in numpositions:
    (j,l,r) = np
    if not(''.join(scheme[j-1][l-1:r+2]) == '.'*(r-l+3) and ''.join(scheme[j+1][l-1:r+2]) == '.'*(r-l+3) and scheme[j][l-1] == '.' and scheme[j][r+1] == '.'): # We have something else besides the dots around the number
        partnumbers.append(compnum(np))

print(sum(partnumbers))

# Part 2

gearsum = 0

for k in range(1,n+1):
    s = scheme[k]
    for i in range(1,n+1):
        if s[i] == '*':
            nums = []
            for np in numpositions:
                (j,l,r) = np
                if k in [j-1,j,j+1] and i >= l-1 and i <= r+1:
                    nums.append(np)
            if len(nums) == 2:
                gearsum += compnum(nums[0])*compnum(nums[1])

print(gearsum)
