from collections import Counter
from functools import cmp_to_key
from copy import copy,deepcopy

# Read and parse the input

with open("input07.txt") as f:
    lines = f.read().splitlines()

hands = []
for l in lines:
    cards,bid = l.split()
    hands.append((cards,int(bid)))

hands2 = deepcopy(hands)

# Part 1

ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

# Return 1 if hand 1 is stronger than hand 2, and -1 otherwise

def compare(hand1,hand2):
    cards1 = hand1[0]
    cards2 = hand2[0]
    cnt1 = Counter(cards1)
    cnt2 = Counter(cards2)
    if len(cnt1) < len(cnt2):
        return(1)
    if len(cnt1) > len(cnt2):
        return(-1)
    # If we reach here, the tupes have equal number of different cards
    if len(cnt1) == 2: # Both are 4 of a kind or full house
        v1 = list(cnt1.values())
        v2 = list(cnt2.values())
        if (4 in v1) and not (4 in v2):
            return(1)
        if not(4 in v1) and (4 in v2):
            return(-1)
    if len(cnt1) == 3: # Both are 3 of a kind or two pair
        v1 = list(cnt1.values())
        v2 = list(cnt2.values())
        if (3 in v1) and not (3 in v2):
            return(1)
        if not(3 in v1) and (3 in v2):
            return(-1)  
    # If we reach here, the hands are of the same type
    for i in range(5):
        if ranks.index(cards1[i]) < ranks.index(cards2[i]):
            return(1)
        if ranks.index(cards1[i]) > ranks.index(cards2[i]):
            return(-1)
    # If there are no equal hands, we should actually never reach here
    return(0)

hands.sort(key=cmp_to_key(compare))

s = 0 

for i in range(len(hands)):
    s += (i+1)*hands[i][1]

print(s)

# Part 2

ranks2 = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']

def dejokerize(cards):
    if not('J' in cards):
        return(cards)
    lc = list(cards)
    lcc = copy(lc)
    while 'J' in lcc:
        lcc.remove('J')
    cnt = Counter(lcc)
    if len(cnt) == 0:
        return('AAAAA')
    if len(cnt) == 1:
        return(lc[0]*5)
    if len(cnt) == 2:
        ckeys = list(cnt.keys())
        if cnt[ckeys[0]] > cnt[ckeys[1]]:
            J = ckeys[0]
        elif cnt[ckeys[0]] < cnt[ckeys[1]]:
            J = ckeys[1]
        elif ranks2.index(ckeys[0]) < ranks2.index(ckeys[1]):
            J = ckeys[0]
        elif ranks2.index(ckeys[0]) > ranks2.index(ckeys[1]):
            J = ckeys[1]
        else:
            print('We should never reach here 1')
    if len(cnt) == 3:
        ckeys = list(cnt.keys())
        if cnt[ckeys[0]] == 2:
            J = ckeys[0]
        elif cnt[ckeys[1]] == 2:
            J = ckeys[1]
        elif cnt[ckeys[2]] == 2:
            J = ckeys[2]        
        elif ranks2.index(ckeys[0]) < ranks2.index(ckeys[1]) and ranks2.index(ckeys[0]) < ranks2.index(ckeys[2]):
            J = ckeys[0]
        elif ranks2.index(ckeys[1]) < ranks2.index(ckeys[0]) and ranks2.index(ckeys[1]) < ranks2.index(ckeys[2]):
            J = ckeys[1]
        elif ranks2.index(ckeys[2]) < ranks2.index(ckeys[0]) and ranks2.index(ckeys[2]) < ranks2.index(ckeys[1]):
            J = ckeys[2]
        else:
            print('We should never reach here 2')
    if len(cnt) == 4:
        ckeys = list(cnt.keys())
        ckeys.sort(key=lambda x: ranks2.index(x))
        J = ckeys[0]
    
    ret = ''
    for c in cards:
        if c == 'J':
            ret += J
        else:
            ret += c

    return(ret)

# Return 1 if hand 1 is stronger than hand 2, and -1 otherwise

def compare2(hand1,hand2):
    cards1 = dejokerize(hand1[0])
    cards2 = dejokerize(hand2[0])
    cnt1 = Counter(cards1)
    cnt2 = Counter(cards2)
    if len(cnt1) < len(cnt2):
        return(1)
    if len(cnt1) > len(cnt2):
        return(-1)
    # If we reach here, the tupes have equal number of different cards
    if len(cnt1) == 2: # Both are 4 of a kind or full house
        v1 = list(cnt1.values())
        v2 = list(cnt2.values())
        if (4 in v1) and not (4 in v2):
            return(1)
        if not(4 in v1) and (4 in v2):
            return(-1)
    if len(cnt1) == 3: # Both are 3 of a kind or two pair
        v1 = list(cnt1.values())
        v2 = list(cnt2.values())
        if (3 in v1) and not (3 in v2):
            return(1)
        if not(3 in v1) and (3 in v2):
            return(-1)  
    # If we reach here, the hands are of the same type
    for i in range(5):
        if ranks2.index(hand1[0][i]) < ranks2.index(hand2[0][i]):
            return(1)
        if ranks2.index(hand1[0][i]) > ranks2.index(hand2[0][i]):
            return(-1)
    # If there are no equal hands, we should actually never reach here
    return(0)

hands2.sort(key=cmp_to_key(compare2))

s = 0 

for i in range(len(hands2)):
    s += (i+1)*hands2[i][1]

print(s)