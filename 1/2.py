#I am confuseder and scareder. Go Go Gadget Arrays!

countyBoi = 0

fileObj = open('1/input.txt', "r")
list = fileObj.read().splitlines()
list = [int(i) for i in list] #oh yes thats sum good good
fileObj.close()

windowSize = 3
i = windowSize
while i < (len(list)):
    previousVal = list[i-1]+list[i-2]+list[i-3]
    currentVal = list[i]+list[i-1]+list[i-2]
    if currentVal > previousVal:
        countyBoi += 1
    i += 1

print(countyBoi)