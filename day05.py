from sys import argv

# Read and parse the input

with open("input05.txt") as f:
    lines = f.read().splitlines()

lines.append('')

seeds = list(map(int,lines[0].split()[1:]))

indices = [i for i, x in enumerate(lines) if x == '']

maps = []

for i in range(len(indices)-1):
    amap = []
    for l in lines[indices[i]+2:indices[i+1]]:
        amap.append(list(map(int,l.split())))
    maps.append(amap)

# Part 1

def applymap(n,amap):
    for ml in amap:
        if n>=ml[1] and n<ml[1]+ml[2]:
            matchfound = True
            return(ml[0]+n-ml[1])
    return(n) # In case none matched

outl=[]

for s in seeds:
    for amap in maps:
        s = applymap(s,amap)
    outl.append(s)

print(min(outl))

# Part 2

# Run the script 10 times as
# python3 day05.py 0
# python3 day05.py 1
# etc
# Having a multi-core processor is helpful.

n = int(argv[1])

minout = 1000000000000

for s in range(seeds[2*n],seeds[2*n]+seeds[2*n+1]):
    for amap in maps:
        s = applymap(s,amap)
    if s < minout:
        minout = s  

print(minout)