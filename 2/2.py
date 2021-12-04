#doin' me a bamboozle, are ya?

horizontalPos = 0
depth = 0
aim = 0

fileObj = open('2/input.txt', "r")
listyBoi = fileObj.read().splitlines()
fileObj.close()

for f in listyBoi:
    split = f.split()
    direction = split[0]
    amount = int(split[1])

    if direction == "forward":
        horizontalPos += amount
        depth += aim * amount
    elif direction == "down":
        aim += amount
    else:
        aim -= amount

print(horizontalPos*depth)