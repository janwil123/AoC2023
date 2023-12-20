from multiprocessing import Pool

# Read and parse the input

with open("input19.txt") as f:
    lines = f.read().splitlines()

workflows = {}
parts = []

for i in range(len(lines)):
    l = lines[i]
    if l == '':
        break
    flowname,commands = l.split('{')
    workflows[flowname] = commands[:-1].split(',')

for j in range(i+1,len(lines)):
    l = lines[j]
    d = {}
    xmas = l[1:-1].split(',')
    for xm in xmas:
        c,n = xm.split('=')
        d[c]=int(n)
    parts.append(d)

segments = {'x':[list(range(1,4001))], 'm':[list(range(1,4001))],'a':[list(range(1,4001))],'s':[list(range(1,4001))]}


for wf in workflows:
    commands = workflows[wf]
    for cmd in commands:
        if '<' in cmd:
            a,b = cmd.split(':')[0].split('<')
            c = int(b)
            for i in range(len(segments[a])):
                if c in segments[a][i]:
                    segments[a] = segments[a][:i] + [list(range(segments[a][i][0],c)),list(range(c,segments[a][i][-1]+1))] + segments[a][(i+1):]
                    break
        if '>' in cmd:
            a,b = cmd.split(':')[0].split('>')
            c = int(b)
            for i in range(len(segments[a])):
                if c in segments[a][i]:
                    segments[a] = segments[a][:i] + [list(range(segments[a][i][0],c+1)),list(range(c+1,segments[a][i][-1]+1))] + segments[a][(i+1):]
                    break

for s in segments:
    segments[s] = [x for x in segments[s] if x!=[]]

# Part 1
    
def runpart(part,cmd):
    workflow = workflows[cmd]
    for action in workflow:
        if action in ['A','R']:
            return(action)
        elif not (':' in action):
            return(runpart(part,action))
        else:
            cond,act = action.split(':')
            if '<' in cond:
                a,b = cond.split('<')
                if part[a] < int(b):
                    if act in ['A','R']:
                        return(act)
                    else:
                        return (runpart(part,act))
            elif '>' in cond:
                a,b = cond.split('>')
                if part[a] > int(b):
                    if act in ['A','R']:
                        return(act)
                    else:
                        return (runpart(part,act))
            else:
                print('We should never reach here')

S = 0
for p in parts:
    res = runpart(p,'in')
    if res == 'A':
        S += (p['x']+p['m']+p['a']+p['s'])

print(S)

# Part 2

def apply_for_sx(sx):
    print(segments['x'].index(sx))
    S = 0
    for sm in segments['m']:
        for sa in segments['a']:
            for ss in segments['s']:
                d = {'x':sx[0],'m':sm[0],'a':sa[0],'s':ss[0]}
                if runpart(d,'in')=='A':
                    S += (sx[-1]-sx[0]+1)*(sm[-1]-sm[0]+1)*(sa[-1]-sa[0]+1)*(ss[-1]-ss[0]+1)
    return(S)

pool = Pool()
res = pool.map(apply_for_sx, segments['x'])
pool.close()

print(sum(res))