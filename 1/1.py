#I am confused and scare someone hold me

previousVal = 0
tally = 0

with open('1/input.txt') as f:
    for line in f:
        currentDepth = line
        if previousVal == 0:
            previousVal = currentDepth
            continue

        if currentDepth > previousVal:
            tally += 1
        previousVal = currentDepth

print(tally+1)