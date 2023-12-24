from fractions import Fraction

# Read and parse the input

pos = []
vel = []
lin = []

with open("input24.txt") as f:
    lines = f.read().splitlines()

for l in lines:
    p,v = l.split(' @ ')
    x,y,z=list(map(int,p.split(', ')))
    vx,vy,vz=list(map(int,v.split(', ')))
    a = vy
    b = -vx
    c = a*x+b*y
    lin.append([a,b,c]) # The equation of the line in the form ax+by=c
    pos.append([x,y,z])
    vel.append([vx,vy,vz])

minb = 200000000000000
maxb = 400000000000000

# Part 1

def det(a11,a12,a21,a22):
    return(a11*a22-a12*a21)

def intersect(i,j):
    x1,y1,z1    = pos[i]
    vx1,vy1,vz1 = vel[i]
    x2,y2,z2    = pos[j]
    vx2,vy2,vz2 = vel[j]
    a1,b1,c1 = lin[i]
    a2,b2,c2 = lin[j]
    detA  = det(a1,b1,a2,b2)
    detAx = det(c1,b1,c2,b2)
    detAy = det(a1,c1,a2,c2)
    if detA == 0:
        if detAx != 0: # Parallel, not coinciding
            return(False) 
        else:
            print('We should not reach here 1')
    x = Fraction(detAx,detA)
    y = Fraction(detAy,detA)
    if (minb <= x <= maxb) and (minb <= y <= maxb) and (x-x1)/vx1 >= 0 and (x-x2)/vx2 >= 0:
        return(True)
    else:
        return(False)
    

s = 0

for i in range(len(lin)-1):
    for j in range(i+1,len(lin)):
        if intersect(i,j):
            s+=1

print(s)

            