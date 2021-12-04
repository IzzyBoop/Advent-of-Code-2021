# I'd like to note that as I'm reading this challenge I said unto myself "this doesnt seem so bad."
# ok this one was a little dirty and theres absolutely a better way to do this but I'll figure it out later. 

fileObj = open('3/input.txt', "r")
listyBoi = fileObj.read().splitlines()
fileObj.close()

gammaArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilonArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bitlength = 12
bit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

k = 0
while k < bitlength:
    for f in listyBoi:
        binArray = []
        for i in f:
            binArray.append(i)
        bit[k] += int(binArray[k])
    k += 1

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

gammaString = ""
epsilonString = ""

for x in gammaArray:
    gammaString += str(x)

for x in epsilonArray:
    epsilonString += str(x)

gammaNum = int(gammaString, 2)
epsilonNum = int(epsilonString, 2)

result = gammaNum * epsilonNum
print(result)