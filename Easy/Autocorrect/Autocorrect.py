
cases = int(input())
for caseNum in range(cases):
    dct, wrds = input()

    diction = []
    for d in range(dct):
        diction.append(input())

    words = []
    for w in range(wrds):
        wrd = input()
        for d in diction:
            for l in wrd:
                pass