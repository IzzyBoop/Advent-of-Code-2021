#I am confuseder and scareder. Go Go Gadget Arrays!

countyBoi = 0

fileObj = open('1/input.txt', "r")
listyBoi = fileObj.read().splitlines()
listyBoi = [int(i) for i in listyBoi] #oh yes thats sum good good
fileObj.close()

windowSize = 3
i = windowSize
while i < (len(listyBoi)):
    previousVal = listyBoi[i-1]+listyBoi[i-2]+listyBoi[i-3]
    currentVal = listyBoi[i]+listyBoi[i-1]+listyBoi[i-2]
    if currentVal > previousVal:
        countyBoi += 1
    i += 1

print(countyBoi)