# Read and parse the input

with open("input12.txt") as f:
    lines = f.read().splitlines()

data = []
nums = []
for l in lines:
    d,n = l.split()
    data.append(d)
    nums.append(tuple(map(int,n.split(','))))

D = {}

def cnt(line,pattern,firstchar):
    if (line,pattern,firstchar) in D:
        return(D[(line,pattern,firstchar)])
    if len(line) == 0 and len(pattern) == 0:
        D[(line,pattern,firstchar)] = 1 
        return(1)
    if len(line) < sum(pattern) + len(pattern) -1 :
        D[(line,pattern,firstchar)] = 0
        return(0)
    if line[0] == '#' and firstchar == '.':
        D[(line,pattern,firstchar)] = 0
        return(0)
    if line[0] == '.' and firstchar == '#':
        D[(line,pattern,firstchar)] = 0
        return(0)
    if len(pattern) == 0:
        if '#' in line:
            D[(line,pattern,firstchar)] = 0
            return(0)        
        else: 
            D[(line,pattern,firstchar)] = 1 
            return(1)  
    if firstchar == '#':
        if line[0] in '?#': 
            if pattern[0] == 1:
                c = cnt(line[1:],pattern[1:],'.')
                D[(line,pattern,firstchar)] = c
                return(c)
            else: 
                np = tuple([pattern[0]-1])+pattern[1:]
                c = cnt(line[1:],np,'#')
                D[(line,pattern,firstchar)] = c
                return(c)
        elif line[0] == '.':
            D[(line,pattern,firstchar)] = 0
            return(0)
    elif firstchar == '.':
        if line[0] in '?.':
            c = cnt(line[1:],pattern,'.') + cnt(line[1:],pattern,'#')
            D[(line,pattern,firstchar)] = c
            return(c)
        elif line[0] == '#':
            D[(line,pattern,firstchar)] = 0
            return(0)            
        
# Part 1

s = 0

for k in range(len(data)):
    s +=  cnt(data[k],nums[k],'.') + cnt(data[k],nums[k],'#')
    
print(s)

# Part 2

s = 0

for k in range(len(data)):
    d = data[k]+'?'+data[k]+'?'+data[k]+'?'+data[k]+'?'+data[k]
    n = nums[k]*5
    s +=  cnt(d,n,'.') + cnt(d,n,'#')

print(s)