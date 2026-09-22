import sys, math
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    alt = int(sys.stdin.readline().rstrip())

    d = (40075 / math.pi) + alt * 2
    cir = d * math.pi

    print(round(cir, 1))