import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    charDict: dict = {}
    line = sys.stdin.readline().rstrip()
    charDict[" "] = 0
    for char in line:
        if char in charDict.keys():
            charDict[char] += 1
        else:
            charDict[char] = 1
    print(line)
    print("-"*len(line))
    print(f"CHARACTERS: {sum(charDict.values())}")
    print(f"WORDS: {charDict[" "]+1}")
    for k in charDict.keys():
        print(f"{k}: {charDict[k]}")
    
