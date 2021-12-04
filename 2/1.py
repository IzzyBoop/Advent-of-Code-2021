#im doing my best, okay?

horizontalPos = 0
depth = 0

fileObj = open('2/input.txt', "r")
listyBoi = fileObj.read().splitlines()
fileObj.close()

for f in listyBoi:
    split = f.split()
    direction = split[0]
    amount = int(split[1])

    if direction == "forward":
        horizontalPos += amount
    elif direction == "down":
        depth += amount
    else:
        depth -= amount

print(horizontalPos*depth)