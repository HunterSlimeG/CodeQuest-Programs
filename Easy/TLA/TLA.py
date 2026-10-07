import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    words = sys.stdin.readline().rstrip().replace("-", " ").split(" ")
    tla = ""

    for w in words:
        for l in w:
            if l.isalpha():
                tla += l
                break
    
    print(tla.upper())
