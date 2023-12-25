import networkx as nx
from random import randint

# Read and parse the input

G = nx.Graph()

with open("input25.txt") as f:
    lines = f.read().splitlines()

for l in lines:
    u,a = l.split(': ')
    vs = a.split()
    for v in vs:
        G.add_edge(u,v,capacity=1)

n = len(G.nodes)

# Part 1

cutfound = False

while not(cutfound):
    i = randint(0,n-1)
    j = randint(0,n-1)
    if i==j:
        continue
    u = (list(G.nodes))[i]
    v = (list(G.nodes))[j]

    cut_value, cut_partition = nx.minimum_cut(G,u,v)
    if cut_value == 3:
        print(len(cut_partition[0])*(len(cut_partition[1])))
        cutfound = True