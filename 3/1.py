# I'd like to note that as I'm reading this challenge I said unto myself "this doesnt seem so bad."
# ok this one was a little dirty and theres absolutely a better way to do this but I'll figure it out later. 

# read file
fileObj = open('3/input.txt', "r")
listyBoi = fileObj.read().splitlines()
fileObj.close()

# starter values
gammaArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilonArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bitlength = 12
bit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# add up the amount of bits in each column that are 1's. 
for f in listyBoi:
    binArray = []

    for i in f:
        binArray.append(i)

    bit[0] += int(binArray[0])
    bit[1] += int(binArray[1])
    bit[2] += int(binArray[2])
    bit[3] += int(binArray[3])
    bit[4] += int(binArray[4])
    bit[5] += int(binArray[5])
    bit[6] += int(binArray[6])
    bit[7] += int(binArray[7])
    bit[8] += int(binArray[8])
    bit[9] += int(binArray[9])
    bit[10] += int(binArray[10])
    bit[11] += int(binArray[11])

# the input file has 1000 entries. So the majority will be any column with 501 bits as either 1 or 0. 
# I can find the majority by dividing the amount of 1's in each column by 1000
# where >0.5 is majority.
# I can then create the gamma and epsilon arrays off this info.
i = 0
while i < bitlength:
    bitmem = int(bit[i])
    
    if (bitmem/1000) < 0.5:
        gammaArray[i] = 0
        epsilonArray[i] = 1
        i += 1
    else:
        gammaArray[i] = 1
        epsilonArray[i] = 0
        i += 1

# starter variables
gammaString = ""
epsilonString = ""

# convert int array to string
for x in gammaArray:
    gammaString += str(x)

for x in epsilonArray:
    epsilonString += str(x)

#convert binary string to decimal int
gammaNum = int(gammaString, 2)
epsilonNum = int(epsilonString, 2)

# multiply for answer
result = gammaNum * epsilonNum
print(result)