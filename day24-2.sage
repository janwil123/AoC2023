# Run this script with SAGE (https://www.sagemath.org/) as
# sage day24-2.sage

# Read and parse the input

xs = [0,0,0]
ys = [0,0,0]
zs = [0,0,0]
vxs = [0,0,0]
vys = [0,0,0]
vzs = [0,0,0]

with open("input24.txt") as f:
    for i in range(3): # We only need three first lines of the input file
        p,v = f.readline().split(' @ ')
        xs[i],ys[i],zs[i]=list(map(int,p.split(', ')))
        vxs[i],vys[i],vzs[i]=list(map(int,v.split(', ')))

# Solve the non-linear system of 9 equations and 9 variables

x,y,z,vx,vy,vz,t1,t2,t3 = var('x,y,z,vx,vy,vz,t1,t2,t3')

sol = solve([x+t1*vx == xs[0]+t1*vxs[0],y+t1*vy == ys[0]+t1*vys[0],z+t1*vz == zs[0]+t1*vzs[0],x+t2*vx == xs[1]+t2*vxs[1],y+t2*vy == ys[1]+t2*vys[1],z+t2*vz == zs[1]+t2*vzs[1],x+t3*vx == xs[2]+t3*vxs[2],y+t3*vy == ys[2]+t3*vys[2],z+t3*vz == zs[2]+t3*vzs[2]],x,y,z,vx,vy,vz,t1,t2,t3,solution_dict=True)

print(sol[0][x]+sol[0][y]+sol[0][z])