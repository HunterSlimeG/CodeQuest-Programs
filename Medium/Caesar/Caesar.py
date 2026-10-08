
cases = int(input())
alph = "abcdefghijklmnopqrstuvwxyz"
for caseNum in range(cases):
    shift = int(input())
    words = input().split(" ")
    newWords = []
    for w in words:
        new = ""
        for l in w:
            new += alph[(alph.find(l)-shift)%26]
        newWords.append(new)
    print(" ".join(newWords))