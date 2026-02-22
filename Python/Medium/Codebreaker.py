import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    alph = dict.fromkeys("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0)
    lines = int(sys.stdin.readline().rstrip())
    for i in range(lines):
        line = sys.stdin.readline().rstrip().upper()
        for l in line:
            if l in alph.keys():
                alph[l] += 1
    for k, v in alph.items():
        count = sum(alph.values())
        if count>0:
            print(f"{k}: {round(((v/count)*100)+0.0001, 2)}%")
        else:
            print(f"{k}: 0.00%")