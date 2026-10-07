import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    dct, wrds = sys.stdin.readline().rstrip()

    diction = []
    for d in range(dct):
        diction.append(sys.stdin.readline().rstrip())

    words = []
    for w in range(wrds):
        wrd = sys.stdin.readline().rstrip()
        for d in diction:
            for l in wrd:
                pass