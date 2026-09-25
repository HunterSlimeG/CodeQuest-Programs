import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    charDict = {}
    line = sys.stdin.readline().rstrip().replace(" ", "")
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