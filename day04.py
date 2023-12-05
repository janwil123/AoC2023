# Read and parse the input

with open("input04.txt") as f:
    lines = f.read().splitlines()

cards = []

for line in lines:
    cardline = line.split(': ')[1]
    setlines = cardline.split(' | ')
    winnums = set(list(map(int,setlines[0].split())))
    mynums = set(list(map(int,setlines[1].split())))
    cards.append([winnums,mynums])

# Part 1

def evalcard(card):
    n = len(card[0].intersection(card[1]))
    if n == 0:
        return(0)
    else:
        return(1<<(n-1))
    
cardsum = 0 

for card in cards:
    cardsum += evalcard(card)

print(cardsum)

# Part 2

n = len(cards)

copies = [1 for _ in range(n)]

for i in range(n):
    wins = len(cards[i][0].intersection(cards[i][1]))
    for j in range(i+1,i+wins+1):
        copies[j] += copies[i]

print(sum(copies))