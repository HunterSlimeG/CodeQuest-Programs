import sys
cases = int(sys.stdin.readline().rstrip())
alph = "abcdefghijklmnopqrstuvwxyz"
for caseNum in range(cases):
    shift = int(sys.stdin.readline().rstrip())
    words = sys.stdin.readline().rstrip().split(" ")
    newWords = []
    for w in words:
        new = ""
        for l in w:
            new += alph[(alph.find(l)-shift)%26]
        newWords.append(new)
    print(" ".join(newWords))