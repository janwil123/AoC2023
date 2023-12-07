# Read and parse the input

with open("input06.txt") as f:
    lines = f.read().splitlines()

times = list(map(int,lines[0].split()[1:]))
dists = list(map(int,lines[1].split()[1:]))

n = len(times)

# Part 1

prod = 1

for s in range(n):
    t = times[s]
    m = 0
    for i in range(t+1):
        if i*(t-i) > dists[s]:
            m+=1
    prod *= m

print(prod)

# Part 2

# OK, now I decided to use my calculator to solve the quadratic inequality x^2−56717999×x+334113513502430 < 0.