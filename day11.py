with open("input11.txt") as f:
    M = f.read().splitlines()

galsinrows = list(map(lambda x:x.count('#'),M))
galsincols = list(map(lambda x:x.count('#'),list(zip(*M))))
gals = sum(galsinrows) # = sum(galsincols)

def cnt(expansion):
    res = 0
    g = 0
    for i in galsincols:
        g += i
        res += g*(gals-g)*(expansion if i==0 else 1)
    g = 0
    for i in galsinrows:
        g += i
        res += g*(gals-g)*(expansion if i==0 else 1)
    return(res)

print(cnt(2))
print(cnt(1000000))