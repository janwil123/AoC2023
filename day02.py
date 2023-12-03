# Read and parse the input

with open("input02.txt") as f:
    lines = f.read().splitlines()

games = []

for line in lines:
    game = []
    cubeline = line.split(': ')[1]
    cubesets = cubeline.split('; ')
    for cs in cubesets:
        cubes = cs.split(', ')
        cubesdict = {}
        for cube in cubes:
            num = int(cube.split(' ')[0])
            colour = cube.split(' ')[1]
            cubesdict[colour]=num
        game.append(cubesdict)
    games.append(game)

# Parts 1 & 2

possiblesum = 0
limits = {'red':12,'green':13,'blue':14}
powersum = 0

for i in range(len(games)):
    game = games[i]
    possible = True
    min_d = {'red':0,'green':0,'blue':0}
    for cubeset in game:
        for colour in cubeset:
            if cubeset[colour] > limits[colour]:
                possible = False
            if cubeset[colour] > min_d[colour]:
                min_d[colour] = cubeset[colour]                           
    if possible:
        possiblesum += i+1
    powersum += min_d['red']*min_d['green']*min_d['blue']

print(possiblesum)
print(powersum)
