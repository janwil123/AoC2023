from math import lcm
from functools import reduce

# Read and parse the input

with open("input08.txt") as f:
    lines = f.read().splitlines()

lrs = lines[0]
n = len(lrs)

commands = {}

for line in lines[2:]:
    start,turns = line.split(' = ')
    left,right = turns[1:-1].split(', ')
    commands[start]=(left,right)

# Part 1

def steps(start):
    i = 0
    node = start
    while node != 'ZZZ':
        lr = lrs[i%n]
        if lr == 'L':
            node = commands[node][0]
        else:
            node = commands[node][1]
        i += 1
    return(i)

print(steps('AAA'))

# Part 2

def steps2(start):
    i = 0
    node = start
    while node[-1] != 'Z':
        lr = lrs[i%n]
        if lr == 'L':
            node = commands[node][0]
        else:
            node = commands[node][1]
        i += 1
    return(i)

As = list(filter(lambda x: x[-1]=='A',commands.keys()))

stepcounts = list(map(steps2,As))

res = reduce(lambda a,b: lcm(a,b),stepcounts,1)

print(res)
