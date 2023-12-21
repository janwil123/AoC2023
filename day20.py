from collections import deque

# Read and parse the input

with open("input20.txt") as f:
    lines = f.read().splitlines()

class Module:
    def __init__(self,type,outs):
        self.type = type
        self.outs = outs
        self.state = False # False for off, True for on
        self.instates = {}

mods = {}

for l in lines:
    name,outputs = l.split(' -> ')
    if name == 'broadcaster':
        module = Module('broadcaster',outputs.split(', '))
        mods['broadcaster'] = module
    elif name[0] == '%':
        module = Module('flip-flop',outputs.split(', '))
        mods[name[1:]] = module         
    elif name[0] == '&':
        module = Module('conjunction',outputs.split(', '))
        mods[name[1:]] = module     

outmods = set()

for m in mods:
    for om in mods[m].outs:
        if not(om in mods):
            outmods.add(om)

for om in outmods:
    outmod = Module('output',[])
    mods[om] = outmod


for m in mods:
    for om in mods[m].outs:
        if not(om in outmods) and mods[om].type == 'conjunction':
            mods[om].instates[m] = False

# Part 1

def push():
    global trues
    global falses
    commands = deque([('broadcaster',False,'button')])
    while commands:
        command = commands.popleft()
        m,signal,origin = command
        if signal:
            trues += 1
        else:
            falses += 1
        match mods[m].type:
            case 'broadcaster':
                for om in mods[m].outs:
                    commands.append((om,False,'broadcaster'))
            case 'flip-flop':
                if signal == False:
                    mods[m].state = not(mods[m].state)
                    for om in mods[m].outs:
                        commands.append((om,mods[m].state,m))
            case 'conjunction':
                mods[m].instates[origin] = signal
                stateconj = True
                for k in mods[m].instates:
                    stateconj = stateconj and mods[m].instates[k]
                for om in mods[m].outs:
                    commands.append((om,not(stateconj),m))      
            case 'output':
                pass          

trues = 0
falses = 0

for _ in range(1000):
    push()

print(trues*falses)

# Part 2

# The input file actually consists of 4 independent sub-schemes. 
# I modified the input file by hand to reflect the sub-schemes and essentially ran the above 
# method four times, resulting in cycles of prime lengths 4073, 4091, 3853 and 4093. 
# So my answer was 4073*4091*3853*4093=262775362119547.