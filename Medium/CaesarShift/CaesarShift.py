
cases = int(input())
alph = "abcdefghijklmnopqrstuvwxyz"
for caseNum in range(cases):
    words = input().lower().split(" ")
    shifts = input().split(" ")
    dirs = input().split(" ")
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