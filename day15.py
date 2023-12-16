# Read and parse the input

with open("input15.txt") as f:
    inp = f.readline().split(',')

# Part 1
    
def HASH(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res = res%256
    return(res)

S = 0

for l in inp:
    S += HASH(l)

print(S)

# Part 2

boxes = [[] for _ in range(256)]

for l in inp:
    if '-' in l:
        label = l[:-1]
        bn = HASH(label)
        for i in range(len(boxes[bn])):
            lens = boxes[bn][i]
            if lens[0] == label:
                boxes[bn] = boxes[bn][:i]+boxes[bn][(i+1):]
                break
    elif '=' in l:
        label,foc = l.split('=')
        bn = HASH(label)
        lensfound = False
        for i in range(len(boxes[bn])):
            lens = boxes[bn][i]
            if lens[0] == label:
                lensfound = True
                boxes[bn][i] = [label,int(foc)]
                break
        if not(lensfound):
            boxes[bn].append([label,int(foc)])

S = 0

for i in range(len(boxes)):
    box = boxes[i]  
    for j in range(len(box)):
        lens = box[j]
        S += (i+1)*(j+1)*lens[1]

print(S)

    

