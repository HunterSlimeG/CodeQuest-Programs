import math
cases = int(input())
for caseNum in range(cases):
    alt = int(input())

    d = (40075 / math.pi) + alt * 2
    cir = d * math.pi

    print(round(cir, 1))