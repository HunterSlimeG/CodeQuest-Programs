import sys
cases = int(sys.stdin.readline().rstrip())
alph = "abcdefghijklmnopqrstuvwxyz"
for caseNum in range(cases):
    words = sys.stdin.readline().rstrip().lower().split(" ")
    shifts = sys.stdin.readline().rstrip().split(" ")
    dirs = sys.stdin.readline().rstrip().split(" ")
    newWords = []
    for w in words:
        new = ""
        for l in w:
            newl = ""
            for s in shifts:
                match dirs[shifts.index(s)]:
                    case "1":
                        newl = alph[(alph.find(l)-int(s))%26]
                    case "0":
                        newl = alph[(alph.find(l)+int(s))%26]
            new += newl
        newWords.append(new)
    print(" ".join(newWords))