
cases = int(input())
for caseNum in range(cases):
    charDict = {}
    line = input()
    words = line.split(" ")
    for l in line:
        if l in charDict.keys():
            charDict[l] += 1
        else:
            charDict[l] = 1
    print(line)
    hy = ""
    for h in range(len(line)):
        hy += "-"
    print(hy)
    print(f"CHARACTERS: {sum(charDict.values())}")
    print(f"WORDS: {len(words)}")
    newDict = {}
    while bool(charDict):
        highest = ""
        for c,v in charDict.items():
            if highest=="" or charDict[c]>charDict[highest]:
                highest = c
        newDict[highest] = charDict.pop(highest)
    for c,v in newDict.items():
        print(f"{c}: {v}")