#I am confuseder and scareder. Go Go Gadget Arrays!

countyBoi = 0

fileObj = open('1/input.txt', "r")
array = fileObj.read().splitlines()
fileObj.close()

windowSize = 3
i = windowSize #current array position (starting at 3)
while i < (len(array)):
    previousVal = int(array[i-1])+int(array[i-2])+int(array[i-3])
    currentVal = int(array[i])+int(array[i-1])+int(array[i-2])
    if currentVal > previousVal:
        countyBoi += 1
    i += 1

print(countyBoi)