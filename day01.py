# Read the input

with open("input01.txt") as f:
    lines = f.readlines()

# Part 1

def findfirstchar(s):
    for c in s:
        if 48 <= ord(c) <= 57:
            return(ord(c)-48)

sum = 0
for line in lines:
    sum += 10*findfirstchar(line) + findfirstchar(line[::-1])

print(sum)

# Part 2

nums = ['zero','one','two','three','four','five','six','seven','eight','nine']

def findfirstcharord(s):
    minpos = len(s)
    minnum = ""
    for num in nums:
        pos = s.find(num)
        if pos >= 0 and pos < minpos:
            minpos = pos
            minnum = num
    for i in range(1,10):
        pos = s.find(str(i))
        if pos >= 0 and pos < minpos:
            minpos = pos         
    if 48 <= ord(s[minpos]) <= 57:
        return(ord(s[minpos])-48)
    else:
        return(nums.index(minnum))
    
revnums = [num[::-1] for num in nums]

def findfirstcharrev(s):
    s = s[::-1]
    minpos = len(s)
    minnum = ""
    for num in revnums:
        pos = s.find(num)
        if pos >= 0 and pos < minpos:
            minpos = pos
            minnum = num
    for i in range(1,10):
        pos = s.find(str(i))
        if pos >= 0 and pos < minpos:
            minpos = pos         
    if 48 <= ord(s[minpos]) <= 57:
        return(ord(s[minpos])-48)
    else:
        return(revnums.index(minnum))
    
sum = 0

for line in lines:
    sum += 10*findfirstcharord(line)+findfirstcharrev(line)

print(sum)