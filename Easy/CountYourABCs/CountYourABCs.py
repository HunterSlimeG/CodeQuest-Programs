
cases = int(input())
for caseNum in range(cases):
    charDict = {}
    line = input().replace(" ", "")
    for l in line:
        if l in charDict.keys():
            charDict[l] += 1
        else:
            charDict[l] = 1
    greatest = 0
    for k in charDict.keys():
        if charDict[k] > greatest:
            greatest = charDict[k]
    print(greatest)